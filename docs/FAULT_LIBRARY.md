# 📚 Fault Library & Simulation Specifications

> **Project 04:** Fake Printer for Testing  
> **Tags:** `SNMP` | `Simulation` | `Windows`  
> **Status:** Week 2 Specification (In Progress)

This document specifies the complete **Fault Library** for the Virtual Printer and Windows PC Fault Agent, detailing how faults are triggered, their observable symptoms (via SNMP, Windows logs, and printer streams), and the exact **Reset & Restore** procedures.

---

## 🖨️ Part 1: Virtual Printer Faults (Device & SNMP)

The virtual printer listens on raw TCP port 9100 and exposes an SNMP agent (UDP port 161) implementing standard Printer MIB (`RFC 3805` / `RFC 1759`) and Host Resources MIB (`RFC 2790`).

| Fault ID | Fault Name | Category | Simulated Symptom | SNMP OID Value | Reset Action |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`PRN_FLT_01`** | **Paper Jam** | Hardware | Printer halts mid-job, rejects new jobs | `hrPrinterDetectedErrorState`: `paperJam(1)` | Set OID to normal (`0`), clear feed roller buffer |
| **`PRN_FLT_02`** | **Out of Paper** | Supply | Printer pauses, sends paper out alert | `hrPrinterDetectedErrorState`: `noPaper(5)` | Set paper tray capacity to 100%, clear alert |
| **`PRN_FLT_03`** | **Low / Out of Toner** | Supply | Warning logged, prints degraded or halts | `prtMarkerSuppliesLevel`: `0` | Reset toner level to `100` |
| **`PRN_FLT_04`** | **Door / Cover Open** | Hardware | Interlocks open, motor disengaged | `hrPrinterDetectedErrorState`: `doorOpen(3)` | Set sensor state to `closed`, reset error state |
| **`PRN_FLT_05`** | **Printer Offline / Disconnected** | Network | TCP connection refused or dropped | Host unresponsive to ping & port 9100 | Re-enable TCP socket listener & network adapter |
| **`PRN_FLT_06`** | **Corrupt Print Stream / Syntax Error** | Protocol | Malformed ESC/POS or PCL stream received | `hrPrinterStatus`: `warning(3)` | Flush print job buffer, discard bad bytes |
| **`PRN_FLT_07`** | **Buffer Overflow / Slowloris** | Transport | Input buffer flooded, slow data burst | `hrPrinterStatus`: `down(5)` | Clear socket input buffer, reset flow control |

---

## 💻 Part 2: Windows Fault Agent (PC Problems)

The Windows Fault Agent simulates real-world client-side PC problems that prevent users from printing or cause jobs to get stuck.

| Fault ID | Fault Name | Target Component | Simulated Symptom | Observable Windows Artifact | Reset Action |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`WIN_FLT_01`** | **Print Spooler Stopped** | Service (`Spooler`) | User cannot print; "RPC server unavailable" | Service `Spooler` status = `Stopped` | Run `net start spooler` (PowerShell `Start-Service Spooler`) |
| **`WIN_FLT_02`** | **Print Spooler Crashed** | Process (`spoolsv.exe`) | Spooler dies during job submission | Windows Event Log Event ID 7034 / 7031 | Clean corrupted `.SHD`/`.SPL` files and restart Spooler |
| **`WIN_FLT_03`** | **Stuck Print Job in Queue** | Spooler Queue | Job status says "Error - Printing", blocks queue | Locked `.SHD` & `.SPL` files in `C:\Windows\System32\spool\PRINTERS` | Stop Spooler, delete `*.spl` / `*.shd`, start Spooler |
| **`WIN_FLT_04`** | **Driver Corrupted / Missing** | Print Driver Subsystem | Print jobs fail silently or prompt driver reinstall | Driver registry key modified or DLL unlinked | Restore driver registry & reinstantiate driver package |
| **`WIN_FLT_05`** | **Port / IP Misconfiguration** | TCP/IP Standard Port | Spooler attempts to connect to wrong IP/port | Printer port set to `192.168.1.254` (non-existent) | Restore printer port to correct virtual printer IP:9100 |
| **`WIN_FLT_06`** | **Printer Set to Offline Mode** | Windows Printer State | Jobs queue up without sending to printer | Printer property `WorkOffline` / `Attributes` has `PRINTER_ATTRIBUTE_WORK_OFFLINE` | Run PowerShell: `Set-Printer -Name "..." -WorkOffline $false` |
| **`WIN_FLT_07`** | **Printer Paused** | Windows Printer State | Jobs held in queue; printer marked "Paused" | Printer state flag `PRINTER_STATUS_PAUSED` | Run PowerShell: `Resume-PrintJob` or unpause printer |

---

## 🔄 Part 3: Reset and Restore Architecture

A core requirement is the ability for the test operator or automated scenario runner to return everything to a known clean state.

```
       ┌───────────────────────────────┐
       │   RESET & RESTORE CONTROLLER  │
       └──────────────┬────────────────┘
                      │
         ┌────────────┴────────────┐
         ▼                         ▼
┌───────────────────┐    ┌───────────────────┐
│  VIRTUAL PRINTER  │    │   WINDOWS AGENT   │
│       RESET       │    │       RESET       │
├───────────────────┤    ├───────────────────┤
│ • Clear buffers   │    │ • Stop Spooler    │
│ • Clear raw jobs  │    │ • Wipe *.SPL/*.SHD│
│ • Reset SNMP OIDs │    │ • Restart Spooler │
│ • Re-open port    │    │ • Fix IP/Port     │
│   9100 listener   │    │ • Unpause/Online  │
└───────────────────┘    └───────────────────┘
```

### 1-Click Clean Baseline Definition:
1. **Virtual Printer:**
   - Listening on `0.0.0.0:9100` (healthy).
   - SNMP agent responding with `hrPrinterStatus = idle(3)` and `hrPrinterDetectedErrorState = 0`.
   - Paper tray full, toner at 100%, cover closed.
2. **Windows Client:**
   - Print Spooler service running (`Running`).
   - `C:\Windows\System32\spool\PRINTERS\` is empty.
   - Printer status is active, online (`WorkOffline = False`), and unpaused.
   - TCP/IP port points to the active virtual printer IP and port 9100.

---

## 🎬 Part 4: Test Scenarios for AI IT-Support Tool

Test scenarios are scripted workflows that trigger a specific sequence of faults, present ticket information to the AI IT-support agent, and verify whether the AI accurately diagnoses and fixes the root cause:

### Scenario 1: "User Cannot Print - Urgent Document"
- **Injected Fault:** `WIN_FLT_01` (Print Spooler Stopped) + `WIN_FLT_03` (Stuck job in spooler).
- **AI Task:** Query Windows service state, detect spooler failure, clear corrupted spool files, and restart service.
- **Verification:** Test job prints successfully after AI resolution.

### Scenario 2: "Printer Showing Error on Network"
- **Injected Fault:** `PRN_FLT_01` (Paper Jam) + SNMP error code active.
- **AI Task:** Query printer via SNMP OID `hrPrinterDetectedErrorState`, identify paper jam, report exact location to user.
- **Verification:** AI suggests paper jam clearance; virtual sensor is cleared.

### Scenario 3: "Jobs Disappearing / Connection Failed"
- **Injected Fault:** `WIN_FLT_05` (Printer IP misconfigured on PC) while virtual printer is healthy.
- **AI Task:** Inspect local port configuration, detect IP mismatch with network printer discovery, update printer port settings.
- **Verification:** Connection re-established and test page printed.
