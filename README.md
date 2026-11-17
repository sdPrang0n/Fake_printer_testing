# Fake Printer for Testing 🖨️

A virtual printer emulator designed for development and automated testing without requiring physical printer hardware.

It emulates a network printer listening on **TCP Port 9100** (JetDirect / RAW / AppSocket protocol), captures incoming print streams (ESC/POS, ZPL, plain text, etc.), and provides:
1. **Raw file captures** (`.bin`) and cleaned human-readable text output (`.txt`).
2. **Real-time console previews** formatted like a printed receipt/page.
3. **Built-in Web Dashboard** on `http://localhost:8080` to inspect captured print jobs visually.
4. **REST API** (`/api/jobs`) for automated test assertions.
5. **Test Client** script to send simulated receipts or custom payloads.

---

## 🚀 Quick Start

### 1. Requirements
- Python 3.8+ (Zero external dependencies — uses Python standard library!)

### 2. Start the Fake Printer Server
```bash
python3 fake_printer.py
```

By default:
- **Printer TCP Listener:** `0.0.0.0:9100`
- **Web Dashboard:** `http://localhost:8080`
- **Saved Print Jobs:** `output_jobs/`

Custom ports can be specified with arguments:
```bash
python3 fake_printer.py --port 9100 --web-port 8080 --output ./my_jobs
```

---

## 🧪 Sending Test Print Jobs

### Using the included Test Client
```bash
# Send a sample formatted receipt
python3 test_client.py

# Send custom plain text
python3 test_client.py --text "Hello from my POS application!"

# Send a raw binary or PRN file
python3 test_client.py --file path/to/sample.bin
```

### Using standard command-line tools
```bash
# Using netcat (nc)
echo "Sample Receipt Line 1" | nc localhost 9100

# Using Telnet
telnet localhost 9100
```

---

## 🌐 Web Dashboard & API

Open your browser to:
```
http://localhost:8080
```
- Auto-refreshes every 3 seconds to display new incoming print jobs.
- Displays job ID, client IP, timestamp, byte size, and full text preview.
- Retrieve jobs as JSON for automated test suites:
  ```bash
  curl http://localhost:8080/api/jobs
  ```

---

## 📁 Repository Structure

```text
Fake_printer_testing/
├── .gitignore          # Ignores captured output files, caches, and system files
├── README.md           # Documentation
├── fake_printer.py     # Main virtual printer server & web viewer
├── test_client.py      # Test script to send sample print jobs
└── output_jobs/        # Directory where incoming print jobs are stored
```

---

## 🔗 Connecting to GitHub

To push this local repository to [sdPrang0n/Fake_printer_testing](https://github.com/sdPrang0n/Fake_printer_testing):

```bash
# 1. Stage and commit files locally
git add .
git commit -m "feat: complete fake printer server with web dashboard and test client"

# 2. Add your GitHub remote repository
git remote add origin https://github.com/sdPrang0n/Fake_printer_testing.git

# 3. Ensure branch is main and push
git branch -M main
git push -u origin main
```
*(If prompted for authentication, enter your GitHub Personal Access Token or use SSH `git@github.com:sdPrang0n/Fake_printer_testing.git`)*
