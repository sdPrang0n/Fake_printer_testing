#!/usr/bin/env python3
"""
Fake Printer Server
A lightweight virtual printer emulator for testing print workflows.
- Raw TCP Socket listener (default port 9100 / JetDirect)
- Captures and stores print jobs as raw binary and cleaned text
- Built-in HTTP web viewer (default port 8080) to inspect print jobs in a browser
"""

import argparse
import datetime
import http.server
import json
import os
import re
import socket
import socketserver
import threading
from typing import List, Dict

OUTPUT_DIR = "output_jobs"
captured_jobs: List[Dict] = []
job_lock = threading.Lock()


def sanitize_esc_pos(data: bytes) -> str:
    """
    Decodes raw printer bytes into human-readable text by:
    - Decoding with latin-1
    - Replacing common ESC/POS / printer control codes
    - Preserving printable ASCII and newlines
    """
    text = data.decode("latin-1", errors="replace")
    # Replace non-printable ASCII control characters except \n, \r, \t
    cleaned = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x9f]", " ", text)
    # Collapse trailing spaces on lines
    cleaned = "\n".join(line.rstrip() for line in cleaned.splitlines())
    return cleaned.strip()


def handle_printer_connection(client_sock: socket.socket, client_addr: tuple, job_id: int):
    client_ip, client_port = client_addr
    print(f"\n📥 [Job #{job_id}] Incoming connection from {client_ip}:{client_port}")

    buffer = bytearray()
    client_sock.settimeout(3.0)  # timeout for idle after data burst

    try:
        while True:
            chunk = client_sock.recv(4096)
            if not chunk:
                break
            buffer.extend(chunk)
    except socket.timeout:
        pass
    except Exception as e:
        print(f"⚠️ [Job #{job_id}] Socket error: {e}")
    finally:
        try:
            client_sock.close()
        except Exception:
            pass

    size = len(buffer)
    if size == 0:
        print(f"⚠️ [Job #{job_id}] Empty payload received from {client_ip}. Ignored.")
        return

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    raw_filename = f"job_{job_id}_{file_ts}.bin"
    txt_filename = f"job_{job_id}_{file_ts}.txt"

    raw_path = os.path.join(OUTPUT_DIR, raw_filename)
    txt_path = os.path.join(OUTPUT_DIR, txt_filename)

    with open(raw_path, "wb") as f:
        f.write(buffer)

    decoded_text = sanitize_esc_pos(buffer)
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(decoded_text)

    job_info = {
        "id": job_id,
        "timestamp": timestamp,
        "client": f"{client_ip}:{client_port}",
        "bytes": size,
        "raw_file": raw_path,
        "txt_file": txt_path,
        "preview": decoded_text[:500] + ("..." if len(decoded_text) > 500 else "")
    }

    with job_lock:
        captured_jobs.append(job_info)

    print(f"✅ [Job #{job_id}] Successfully captured {size} bytes")
    print(f"   Saved raw binary: {raw_path}")
    print(f"   Saved text:       {txt_path}")
    print("┌" + "─" * 46 + "┐")
    print("│ PRINT OUTPUT PREVIEW                         │")
    print("├" + "─" * 46 + "┤")
    for line in decoded_text.splitlines()[:15]:
        print(f"│ {line[:44]:<44} │")
    if len(decoded_text.splitlines()) > 15:
        print("│ ... [truncated in console preview]           │")
    print("└" + "─" * 46 + "┘\n")


def start_printer_server(host: str, port: int):
    """Starts the TCP socket server on the printer port."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((host, port))
    server.listen(10)
    print(f"🖨️  Fake Printer TCP Server running on {host}:{port}")

    job_id = 1
    while True:
        try:
            client_sock, client_addr = server.accept()
            worker = threading.Thread(
                target=handle_printer_connection,
                args=(client_sock, client_addr, job_id),
                daemon=True
            )
            worker.start()
            job_id += 1
        except Exception as e:
            print(f"Server loop error: {e}")
            break


class WebViewerHandler(http.server.BaseHTTPRequestHandler):
    """HTTP handler to view captured jobs in a browser or fetch via JSON."""
    def do_GET(self):
        if self.path == "/api/jobs":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            with job_lock:
                data = json.dumps(captured_jobs, indent=2)
            self.wfile.write(data.encode("utf-8"))
            return

        # HTML Dashboard
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()

        with job_lock:
            jobs_reversed = list(reversed(captured_jobs))

        rows_html = ""
        for job in jobs_reversed:
            preview_escaped = (
                job["preview"]
                .replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
            )
            rows_html += f"""
            <div class="job-card">
                <div class="job-header">
                    <span class="badge">Job #{job['id']}</span>
                    <span><strong>Received:</strong> {job['timestamp']}</span>
                    <span><strong>From:</strong> {job['client']}</span>
                    <span><strong>Size:</strong> {job['bytes']} bytes</span>
                </div>
                <pre class="preview">{preview_escaped}</pre>
                <div class="files">
                    Files: <code>{job['raw_file']}</code> | <code>{job['txt_file']}</code>
                </div>
            </div>
            """

        if not rows_html:
            rows_html = "<p style='color: #888;'>No print jobs received yet. Send a job to port 9100!</p>"

        html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Fake Printer Dashboard</title>
    <meta http-equiv="refresh" content="3">
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background: #0f172a; color: #f8fafc; margin: 0; padding: 20px; }}
        header {{ display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #334155; padding-bottom: 15px; margin-bottom: 20px; }}
        h1 {{ margin: 0; font-size: 24px; }}
        .status {{ background: #22c55e; color: #000; padding: 4px 10px; border-radius: 999px; font-size: 13px; font-weight: bold; }}
        .job-card {{ background: #1e293b; border-radius: 8px; padding: 16px; margin-bottom: 16px; border: 1px solid #334155; }}
        .job-header {{ display: flex; gap: 20px; margin-bottom: 10px; font-size: 14px; color: #cbd5e1; align-items: center; }}
        .badge {{ background: #3b82f6; color: white; padding: 2px 8px; border-radius: 4px; font-weight: bold; }}
        pre.preview {{ background: #090d16; color: #38bdf8; padding: 12px; border-radius: 6px; overflow-x: auto; font-family: ui-monospace, Menlo, Consolas, monospace; font-size: 13px; margin: 0 0 10px 0; white-space: pre-wrap; }}
        .files {{ font-size: 12px; color: #94a3b8; }}
        code {{ background: #334155; padding: 2px 6px; border-radius: 4px; }}
    </style>
</head>
<body>
    <header>
        <div>
            <h1>🖨️ Fake Printer Dashboard</h1>
            <p style="margin: 4px 0 0; color: #94a3b8; font-size: 13px;">Auto-refreshes every 3 seconds | API at <a href="/api/jobs" style="color: #60a5fa;">/api/jobs</a></p>
        </div>
        <div class="status">● LISTENING</div>
    </header>
    <main>
        {rows_html}
    </main>
</body>
</html>
"""
        self.wfile.write(html.encode("utf-8"))

    def log_message(self, format, *args):
        # Silence access logs for web viewer to keep terminal clean
        return


def start_web_server(host: str, port: int):
    """Starts the Web UI dashboard on the given port."""
    class ReuseServer(socketserver.ThreadingTCPServer):
        allow_reuse_address = True

    try:
        with ReuseServer((host, port), WebViewerHandler) as httpd:
            print(f"🌐 Fake Printer Web Dashboard: http://localhost:{port}")
            httpd.serve_forever()
    except Exception as e:
        print(f"⚠️ Web Dashboard error: {e}")


def main():
    global OUTPUT_DIR
    parser = argparse.ArgumentParser(description="Fake Printer Server for Testing")
    parser.add_argument("--host", default="0.0.0.0", help="Host interface to bind (default: 0.0.0.0)")
    parser.add_argument("--port", type=int, default=9100, help="Printer TCP port (default: 9100)")
    parser.add_argument("--web-port", type=int, default=8080, help="Web dashboard port (default: 8080, 0 to disable)")
    parser.add_argument("--output", default=OUTPUT_DIR, help="Directory to save print jobs")
    args = parser.parse_args()

    OUTPUT_DIR = args.output
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Launch Web Server thread if enabled
    if args.web_port > 0:
        web_thread = threading.Thread(
            target=start_web_server,
            args=(args.host, args.web_port),
            daemon=True
        )
        web_thread.start()

    # Run Printer Server on main thread
    start_printer_server(args.host, args.port)


if __name__ == "__main__":
    main()
