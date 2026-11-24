# 📚 Fault Library & Simulation Specifications

> **Project:** Fake Printer for Testing Event Management and AI Support Application  
> **Course:** SCI 700 / SCI 701  
> **Tags:** `SNMP` | `Simulation` | `Windows`  
> **Status:** Week 2 Specification (In Progress)

This document specifies the complete **Fault Library** for the Virtual Printer Device, the **SNMP Trap Generator**, and the **Windows Endpoint Fault Agent** (Windows 11 VM), along with the **Reset and Restore Mechanism** designed to benchmark an AI IT-support platform.

---

## 🖨️ Part 1: Virtual Printer Fault Library (Debian/Ubuntu Host)

The virtual printer runs on the Debian/Ubuntu simulation host, listening on TCP port 9100 and hosting an SNMP Agent (`RFC 3805` Printer MIB / `RFC 1759`).

| Fault ID | Fault Name | Category | Simulated Condition | SNMP OID Value / Status | Reset Action |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`PRN_FLT_01`** | **Paper Tray Status: Paper Jam** | Paper Tray | Sensor detects paper stuck in feed rollers; printing halted | `hrPrinterDetectedErrorState`: `paperJam(1)` | Clear feed path buffer, set OID to normal (`0`) |
| **`PRN_FLT_02`** | **Paper Tray Status: Paper Out** | Paper Tray | Paper tray sensor indicates empty tray; jobs queued | `hrPrinterDetectedErrorState`: `noPaper(5)` | Refill virtual paper tray capacity to 100% |
| **`PRN_FLT_03`** | **Toner Level: Low Toner** | Consumables | Toner level drops below 10% threshold; warning state | `prtMarkerSuppliesLevel`: `10` (Warning) | Restore toner level to `100` |
| **`PRN_FLT_04`** | **Toner Level: Empty / Missing** | Consumables | Toner depleted or cartridge unseated; printer halts | `prtMarkerSuppliesLevel`: `0`, `hrPrinterStatus`: `down(5)` | Reset cartridge status to present, level to `100` |
| **`PRN_FLT_05`** | **Print Cover Open** | Hardware | Interlock sensor open on top/front maintenance cover | `hrPrinterDetectedErrorState`: `doorOpen(3)` | Set cover sensor state to `closed`, clear error |
| **`PRN_FLT_06`** | **Bad Network: Port 9100 Offline** | Network | TCP connection refused or dropped; printer unreachable | Port 9100 closed, ping responds | Re-open TCP socket listener on port 9100 |
| **`PRN_FLT_07`** | **Bad Network: Latency & Packet Drop** | Network | High packet delay or intermittent connection drops | Intermittent TCP timeout during payload stream | Reset virtual network bridge traffic shaping |
| **`PRN_FLT_08`** | **Corrupt Print Stream / Malformed ESC-POS** | Protocol | Malformed escape codes or truncated raster graphics stream | `hrPrinterStatus`: `warning(3)` | Flush print job buffer, discard bad bytes |

---

## 📡 Part 2: SNMP Trap Generator (Event Management Integration)

To simulate proactive enterprise alert generation for event management systems and AI IT-support monitoring, the **SNMP Trap Generator** transmits asynchronous notifications (`SNMPv2c TRAP` / `INFORM`) when faults occur:

| Trap ID | Trigger Event | Trap OID / Enterprise OID | Trap Payload Objects (Varbinds) |
| :--- | :--- | :--- | :--- |
| **`TRAP_01`** | Paper Jam Detected | `1.3.6.1.4.1.9999.1.1` (`prnPaperJamTrap`) | `hrPrinterDetectedErrorState` = `paperJam`, Location = "Tray 1" |
| **`TRAP_02`** | Toner Depleted | `1.3.6.1.4.1.9999.1.2` (`prnTonerEmptyTrap`) | `prtMarkerSuppliesLevel` = 0, SupplyType = "Black Toner" |
| **`TRAP_03`** | Cover Interlock Opened | `1.3.6.1.4.1.9999.1.3` (`prnCoverOpenTrap`) | `hrPrinterDetectedErrorState` = `doorOpen`, Cover = "Front Door" |
| **`TRAP_04`** | Device Offline / Heartbeat Lost | `1.3.6.1.4.1.9999.1.4` (`prnOfflineTrap`) | `hrPrinterStatus` = `down(5)`, LastKnownIP = IP address |
| **`TRAP_05`** | Printer Normal / Cleared | `1.3.6.1.4.1.9999.1.0` (`prnNormalTrap`) | `hrPrinterStatus` = `idle(3)`, `hrPrinterDetectedErrorState` = 0 |

---

## 💻 Part 3: Windows Endpoint Fault Agent (Windows 11 VM)

The Windows Endpoint Fault Agent runs on the demo Windows 11 VM, controlling key operating system services and print subsystem states:

| Fault ID | Fault Name | Target Component | Simulated Symptom | Observable Windows Artifact | Reset Action |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`WIN_FLT_01`** | **Print Spooler Service Stopped** | Windows Service (`Spooler`) | User cannot print; error "The print spooler service is not running" | Service `Spooler` status = `Stopped` | Execute `Start-Service Spooler` (PowerShell / Win32 API) |
| **`WIN_FLT_02`** | **Print Spooler Crash / Abnormal Exit** | Process (`spoolsv.exe`) | Spooler terminates abruptly when job submitted | Windows Application Event Log Event ID 7034 / 7031 | Clean corrupted `.SHD`/`.SPL` files and restart Spooler |
| **`WIN_FLT_03`** | **Stuck Print Job in Spooler Queue** | Spooler Queue Storage | Jobs stuck in "Deleting - Printing" state, blocking all queue | Locked `.SHD` & `.SPL` files in `C:\Windows\System32\spool\PRINTERS` | Stop Spooler, purge `*.spl` / `*.shd`, start Spooler |
| **`WIN_FLT_04`** | **Corrupted / Missing Printer Driver** | Driver Subsystem | Jobs fail silently or system prompts driver reinstallation | Registry key unlinked or core driver DLL renamed | Restore driver package and re-link print driver registry |
| **`WIN_FLT_05`** | **Port / IP Misconfiguration** | TCP/IP Standard Port | Spooler attempts to connect to unreachable/wrong IP:port | Port registry points to invalid host `192.168.1.254` | Reset printer port to virtual printer IP (e.g., `192.168.1.100:9100`) |
| **`WIN_FLT_06`** | **Printer Set to "Use Printer Offline"** | Printer State Attribute | Print jobs queue up locally without transmitting | Printer attribute flag `PRINTER_ATTRIBUTE_WORK_OFFLINE` | Execute `Set-Printer -Name "..." -WorkOffline $false` |

---

## 🔄 Part 4: Reset and Restore Mechanism

A primary requirement of the customer is **repeatability**—the ability to reset the entire test environment back to a clean baseline in seconds after an AI demo.

```
                  ┌─────────────────────────────────┐
                  │   RESET & RESTORE CONTROLLER    │
                  └───────────────┬─────────────────┘
                                  │
         ┌────────────────────────┴────────────────────────┐
         ▼                                                 ▼
┌─────────────────────────────────┐       ┌─────────────────────────────────┐
│ DEBIAN HOST / VIRTUAL PRINTER   │       │   WINDOWS 11 DEMO VM AGENT      │
├─────────────────────────────────┤       ├─────────────────────────────────┤
│ • Clear socket buffers & jobs   │       │ • Stop `Spooler` service        │
│ • Reset SNMP OIDs to normal (0) │       │ • Wipe `spool\PRINTERS\*.spl`   │
│ • Clear paper jam / cover flags │       │ • Restore driver & port mapping │
│ • Set toner level to 100%       │       │ • Restart `Spooler` service     │
│ • Emit SNMP Trap 'prnNormalTrap'│       │ • Set `WorkOffline = False`     │
└─────────────────────────────────┘       └─────────────────────────────────┘
```

### Clean Baseline Verification Criteria:
1. **Virtual Printer (Debian/Ubuntu):**
   - Listening on TCP port `9100`.
   - SNMP agent responding: `hrPrinterStatus = idle(3)` and `hrPrinterDetectedErrorState = 0`.
   - Toner level = 100%, Paper tray = full, Cover = closed.
2. **Windows 11 VM:**
   - Print Spooler service state = `Running`.
   - Queue directory `C:\Windows\System32\spool\PRINTERS\` is empty.
   - Printer status is Online (`WorkOffline = False`) and unpaused.
   - Standard TCP/IP port points to Virtual Printer IP on port 9100.

---

## 🎯 Alignment with the 7 Core Requirements

| Core Requirement | Implementation in Fault Library & Reset System |
| :--- | :--- |
| **Repeatability** | Deterministic fault triggers and automated 1-click restore mechanism guarantee identical test conditions on every run. |
| **Realism** | Standard RFC 3805 SNMP MIB values, real Windows Spooler services, and genuine TCP 9100 streams. |
| **Controllability** | Fine-grained parameter control (e.g., specific toner percentage, cover sensor toggle, network latency milliseconds). |
| **Isolation and safety** | Sandbox execution in Debian VM and Windows 11 demo VM prevents damage to host or production hardware. |
| **Portability** | VM and container-compatible design deployable on local workstations without cloud or external dependencies. |
| **Observability** | Comprehensive state logging, SNMP trap generation, and real-time Web Control Interface. |
| **Extensibility** | Pluggable fault definitions allowing new printer models, SNMP traps, or Windows service faults to be added easily. |
