#!/usr/bin/env python3
"""
Test Client for Fake Printer
Sends sample print jobs (text or simulated ESC/POS receipt) to test the fake printer.
"""

import argparse
import socket
import sys
import time

SAMPLE_RECEIPT = b"""\x1b\x40
========================================
           TEST COFFEE SHOP
        123 Virtual Lane, Cloud
========================================
Date: 2026-11-17 11:30 AM
Receipt #: 98765
Cashier: Alice
----------------------------------------
ITEM                        PRICE
----------------------------------------
1x Espresso                 $3.50
1x Croissant                $4.20
1x Oat Milk Flat White      $5.00
----------------------------------------
Subtotal:                  $12.70
Tax (10%):                  $1.27
TOTAL:                     $13.97
----------------------------------------
Payment Method: VISA (**** 4321)
Approval Code: 123456

       Thank you for your order!
        Visit again soon!
========================================
\x1d\x56\x00
"""

def send_print_job(host: str, port: int, payload: bytes):
    print(f"Connecting to fake printer at {host}:{port}...")
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(5.0)
            sock.connect((host, port))
            sock.sendall(payload)
            time.sleep(0.1)  # small delay before closing
        print(f"✅ Successfully sent {len(payload)} bytes to {host}:{port}")
    except ConnectionRefusedError:
        print(f"❌ Connection failed: Is the fake printer running on {host}:{port}?", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error sending print job: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Send test print job to Fake Printer")
    parser.add_argument("--host", default="127.0.0.1", help="Printer host (default: 127.0.0.1)")
    parser.add_argument("--port", type=int, default=9100, help="Printer port (default: 9100)")
    parser.add_argument("--file", help="Path to custom file or binary payload to send")
    parser.add_argument("--text", help="Plain text message to print")
    args = parser.parse_args()

    if args.file:
        with open(args.file, "rb") as f:
            data = f.read()
    elif args.text:
        data = args.text.encode("utf-8") + b"\n\n"
    else:
        # Default sample receipt
        data = SAMPLE_RECEIPT

    send_print_job(args.host, args.port, data)

if __name__ == "__main__":
    main()
