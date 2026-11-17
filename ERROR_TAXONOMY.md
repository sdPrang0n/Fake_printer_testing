# 🔍 Virtual Printer Error Taxonomy & Detection Specifications

This document defines the formal classification, schemas, and detection criteria for errors that the **Virtual Printer** system will identify and simulate throughout the 12-week project.

---

## 1. Error Categories Overview

| Code Prefix | Category | Description |
| :--- | :--- | :--- |
| `NET_ERR_` | **Network & Transport** | Connection drops, timeouts, socket resets, and stream stalls |
| `PROTO_ERR_` | **Protocol & Syntax** | Malformed ESC/POS, ZPL, or line printer control codes |
| `DATA_ERR_` | **Data & Integrity** | Corrupted payloads, encoding mismatches, and truncation |
| `HW_ERR_` | **Hardware Emulation** | Simulated device faults (out of paper, cover open, head jam) |

---

## 2. Detailed Error Taxonomy

### 🌐 A. Network & Transport Errors (`NET_ERR_`)

#### `NET_ERR_01: CONNECTION_TIMEOUT`
- **Description:** Client initiates connection but halts transmission before sending a complete print job or header.
- **Detection Trigger:** Inactive socket duration exceeds the configured threshold (e.g., 5 seconds) without receiving an EOF or job termination sequence.
- **Severity:** Medium

#### `NET_ERR_02: ABRUPT_SOCKET_TERMINATION`
- **Description:** Client abruptly resets or closes the TCP connection in the middle of a print stream.
- **Detection Trigger:** Socket receives `ECONNRESET` or unexpected zero-byte read while in the middle of reading a declared payload length.
- **Severity:** High

#### `NET_ERR_03: BUFFER_OVERFLOW`
- **Description:** Incoming print payload exceeds maximum allowable memory buffer.
- **Detection Trigger:** Buffered bytes exceed configured memory threshold (e.g., > 10MB for receipt printer).
- **Severity:** High

---

### 📜 B. Protocol & Syntax Errors (`PROTO_ERR_`)

#### `PROTO_ERR_01: INVALID_ESCAPE_SEQUENCE`
- **Description:** Stream contains unrecognized escape commands or invalid command parameters.
- **Detection Trigger:** Parser encounters `0x1B` (ESC) or `0x1D` (GS) followed by non-standard or unsupported command bytes.
- **Severity:** Medium

#### `PROTO_ERR_02: TRUNCATED_COMMAND_PARAMETERS`
- **Description:** A multi-byte command sequence (such as barcode data or raster graphics) terminates before providing declared byte count.
- **Detection Trigger:** Command specifies payload length $N$, but stream ends after $M < N$ bytes.
- **Severity:** High

#### `PROTO_ERR_03: MISSING_JOB_INITIALIZATION`
- **Description:** Stream sends raw graphics or print commands without prior printer initialization (`ESC @`).
- **Detection Trigger:** Absence of initialization sequence at the start of a new connection session.
- **Severity:** Low / Warning

---

### 🔠 C. Data & Encoding Integrity Errors (`DATA_ERR_`)

#### `DATA_ERR_01: ENCODING_MISMATCH`
- **Description:** Payload contains byte sequences that are invalid for the active code page or encoding.
- **Detection Trigger:** Character decoder fails strict decoding (e.g., invalid UTF-8 multibyte sequence or unmapped codepage bytes).
- **Severity:** Medium

#### `DATA_ERR_02: PAYLOAD_TRUNCATION`
- **Description:** Incomplete print job where final cut command (`GS V`) or end-of-transmission (`EOT`) is missing.
- **Detection Trigger:** Socket closes normally but expected delimiter / cut command was not reached.
- **Severity:** Medium

#### `DATA_ERR_03: CORRUPTED_BITMAP_RASTER`
- **Description:** Raster image bitstream contains incomplete scan lines or byte misalignments.
- **Detection Trigger:** Calculated raster dimensions do not match the byte count provided in the graphics header.
- **Severity:** High

---

### ⚠️ D. Simulated Hardware Faults (`HW_ERR_`)

#### `HW_ERR_01: OUT_OF_PAPER`
- **Description:** Virtual printer simulates a paper-out condition to test client error recovery.
- **Return Status:** Real-time status response with paper-out flag active (`0x10 0x04 0x04`).

#### `HW_ERR_02: COVER_OPEN`
- **Description:** Simulates printer cover being open during an active job.
- **Return Status:** Status response flag set (`0x10 0x04 0x01`).

#### `HW_ERR_03: HEAD_OVERHEAT_OR_JAM`
- **Description:** Simulates thermal print head overheating or cutter jam.
- **Return Status:** Error status bit set (`0x10 0x04 0x02`).

---

## 3. Standard Diagnostic Report Schema

When an error is detected, the Virtual Printer produces a standardized JSON diagnostic record:

```json
{
  "job_id": 104,
  "timestamp": "2026-11-17T12:00:00Z",
  "client_ip": "192.168.1.50:54321",
  "error_code": "PROTO_ERR_02",
  "error_category": "PROTOCOL_SYNTAX",
  "severity": "HIGH",
  "message": "Command GS v 0 declared 128 bytes, but stream terminated after 42 bytes",
  "byte_offset": 84,
  "raw_hex_snippet": "1d 76 30 00 10 00 08 00 ...",
  "suggested_fix": "Verify raster image generation logic and stream flush operations on client side."
}
```
