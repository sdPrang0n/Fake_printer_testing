# 📋 System Requirements Specification (SRS)

> **Project Title:** Fake Printer for Testing Event Management and AI Support Application  
> **Course Codes:** SCI 700 / SCI 701 — Industry Project / Capstone  
> **Institution:** University of the Sunshine Coast (UniSC)  
> **Team:** Team 04 (2 Members)  
> **Repository:** [sdPrang0n/Fake_printer_testing](https://github.com/sdPrang0n/Fake_printer_testing)  
> **Tags:** `SNMP` | `Simulation` | `Windows`

---

## 1. Executive Summary & Client Context

### 1.1 Client Problem Statement
The customer markets an **AI Support Platform** engineered to autonomously diagnose, troubleshoot, and remediate technical IT issues on end-users' computers without requiring a human service desk agent to contact the customer.

During live sales demonstrations and client proof-of-concept (PoC) evaluations, the primary operational challenge is demonstrating the system actually fixing a problem in real time. Intentionally "breaking" live, physical production devices or enterprise printers is:
1. **Risky:** Potential for unrecoverable system corruption or network outages.
2. **Expensive:** Consumables wastage (paper, toner, physical hardware maintenance).
3. **Non-Repeatable:** Real hardware failures cannot be triggered on cue or deterministically reset during a 30-minute sales pitch.

### 1.2 Proposed Solution
Team 04 is designing and deploying a **safe, isolated, virtual testing and troubleshooting environment** consisting of a **Debian/Ubuntu Simulation Host VM** and a **Windows 11 Demo Client VM**. This platform allows operators to simulate realistic printer and PC failures on demand, monitor event flows into the AI support platform, and execute a one-click reset to clean baselines for repeatable demonstrations.

---

## 2. System Architecture & Topology

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       SIMULATION HOST (Debian / Ubuntu VM)                  │
│                                                                             │
│  ┌────────────────────────┐  ┌────────────────────────┐  ┌───────────────┐  │
│  │  Virtual Printer       │  │  SNMP Agent & MIB      │  │ SNMP Trap     │  │
│  │  Device (TCP 9100/IPP) │  │  (RFC 3805 / RFC 1759) │  │ Generator     │  │
│  └───────────▲────────────┘  └───────────▲────────────┘  └───────┬───────┘  │
│              │                           │                       │          │
│  ┌───────────┴───────────────────────────┴────────────┐          │ (Traps)  │
│  │             Printer Fault Library                  │          │          │
│  │  (Bad Network, Toner, Paper Tray, Cover Open)      │          │          │
│  └────────────────────────────────────────────────────┘          │          │
│                                                                  │          │
│  ┌────────────────────────────────────────────────────┐          │          │
│  │            Web Control Interface & API             │          │          │
│  │    (Control errors, timing, and scenario runs)     │          │          │
│  └───────────────────────┬────────────────────────────┘          │          │
│                          │                                       │          │
│  ┌───────────────────────┴────────────────────────────┐          │          │
│  │     Scenario Engine & State Monitoring/Logging     │          │          │
│  └───────────────────────┬────────────────────────────┘          │          │
│                          │                                       │          │
│  ┌───────────────────────┴────────────────────────────┐          │          │
│  │        Reset & Restore Subsystem Controller        │          │          │
│  └───────────────────────┬────────────────────────────┘          │          │
└──────────────────────────┼───────────────────────────────────────┼──────────┘
                           │ (Control / RPC)                       │
                           ▼                                       ▼
┌────────────────────────────────────────────────────────┐  ┌─────────────────┐
│              DEMO CLIENT (Windows 11 VM)               │  │  AI IT SUPPORT  │
│                                                        │  │    PLATFORM     │
│  ┌──────────────────────────────────────────────────┐  │  │   (Customer)    │
│  │ Windows Endpoint Fault Agent                     │  │  └────────▲────────┘
│  │ • Print Spooler (`spoolsv.exe`) Service Control  │  │           │
│  │ • Stuck Queue Manipulator (`*.SPL`, `*.SHD`)     │  │           │
│  │ • Port & Driver Misconfiguration Simulator       │──┼───────────┘
│  └──────────────────────────────────────────────────┘  │ (Telemetry & Events)
└────────────────────────────────────────────────────────┘
```

---

## 3. The 12 Project Deliverables (Functional Specifications)

The 12 deliverables identified in the project requirements grid are detailed below:

### 1. Simulation Host Environment
- **Platform:** Debian 12 / Ubuntu 22.04 LTS Virtual Machine.
- **Role:** Centralized hosting platform for the virtual printer service, SNMP daemon, Web Control Interface, Scenario Engine, and logging subsystems.
- **Specification:** Headless Linux environment with network bridging to the Windows 11 demo VM.

### 2. Virtual Printer Device
- **Protocol Support:** Raw TCP Port 9100 (JetDirect / AppSocket) and IPP (Internet Printing Protocol).
- **Capability:** Ingests print jobs, decodes command streams (ESC/POS, PCL, PostScript, plain text), and renders or stores job payloads without requiring physical hardware.

### 3. SNMP Agent and Printer MIB Implementation
- **Standards:** RFC 3805 (Printer MIB v2), RFC 1759 (Printer MIB v1), and RFC 2790 (Host Resources MIB).
- **Functionality:** Listens on UDP port 161. Responds to SNMP `GET`, `GETNEXT`, and `WALK` requests from the AI support tool to report device status, model info, and telemetry.

### 4. Printer Fault Library
- **Scope:** Configurable hardware and network fault modules:
  - *Bad Network:* Socket disconnects, dropped packets, simulated latency, port closure.
  - *Toner Levels:* Low toner warning (<10%), depleted toner (0%), cartridge missing.
  - *Paper Tray Status:* Paper jam in tray/rollers, paper out / empty tray, wrong paper size.
  - *Print Cover Open:* Top cover interlock open, front door unlatched.
  - *Stream Errors:* Truncated jobs, corrupt control bytes.

### 5. SNMP Trap Generator
- **Protocol:** SNMPv2c / SNMPv3 Trap and Inform notifications on UDP port 162.
- **Behavior:** Proactively dispatches alert packets to the customer's event management system when a fault is triggered (e.g., immediate notification of paper jam or cover open).

### 6. Windows Endpoint Fault Agent
- **Target OS:** Windows 11 (64-bit) Demo Virtual Machine.
- **Architecture:** Lightweight agent (PowerShell / Python / C# background service) communicating securely with the Simulation Host.
- **Capability:** Manipulates Windows services, registry keys, driver states, and spooler file directories.

### 7. Endpoint Fault Library
- **Simulated Windows Issues:**
  - *Spooler Stopped:* Stop the Windows `Spooler` service (`spoolsv.exe`).
  - *Spooler Crashed:* Force-kill the spooler process during active print submission.
  - *Stuck Queue:* Lock corrupted `.SPL` and `.SHD` files in `C:\Windows\System32\spool\PRINTERS`.
  - *Driver Faults:* Corrupt or unregister printer driver packages.
  - *Port Misconfiguration:* Redirect printer port to an invalid IP address.
  - *Offline Mode:* Set Windows printer property `WorkOffline = True`.

### 8. Reset and Restore Mechanism
- **Goal:** Deterministic 1-click restore to a clean baseline within 5 seconds.
- **Printer Reset:** Empty buffers, restore toner to 100%, reset all SNMP OIDs to healthy (`0`), close and latch covers, restart port 9100 listener.
- **Windows Reset:** Restart `Spooler` service, purge all spooler directory files, reset printer port and online flags, verify print queue is clear.

### 9. Web Control Interface
- **User Interface:** Clean, responsive browser-based dashboard.
- **Controls:**
  - Interactive fault toggles (1-click trigger for paper jam, low toner, spooler stop, etc.).
  - Timing controls to schedule when errors occur during a live demo.
  - Live status indicator displaying current printer and PC health states.
  - Scenario selection and execution buttons.

### 10. Scenario Engine
- **Orchestration:** Scriptable JSON/YAML test case sequencer.
- **Functionality:** Executes multi-stage incidents (e.g., Step 1: Start print job ➔ Step 2: Stop Spooler after 2 seconds ➔ Step 3: Trigger SNMP Trap ➔ Step 4: Wait for AI diagnostic resolution ➔ Step 5: Verify resolution).

### 11. State Monitoring and Logging
- **Telemetry:** Real-time log streamer and event capture.
- **Observability:** Centralized view of all injected faults, client print attempts, SNMP queries, and reset operations with millisecond timestamps.

### 12. Deployment and Operating
- **Distribution:** Infrastructure-as-Code (IaC) setup scripts, Docker/Vagrant VM configurations, and comprehensive Operating Guide for seamless demonstration deployment on developer laptops.

---

## 4. The 7 Core Project Requirements (Acceptance Criteria)

| Requirement | Technical Definition | Verification & Acceptance Criteria |
| :--- | :--- | :--- |
| **1. Repeatability** | Identical test inputs always produce identical symptoms, error codes, and recovery states. | Run 20 consecutive cycles of Scenario 1 (Spooler crash + Restore); verify 100% identical state transitions without manual intervention. |
| **2. Realism** | Simulated components are indistinguishable from genuine enterprise printers and Windows 11 PCs. | The AI IT-Support platform diagnoses virtual faults using standard RFC 3805 SNMP queries and Windows Win32 APIs without custom test hooks. |
| **3. Controllability** | Operators can specify exact fault parameters, combinations, and trigger timelines. | Operators can inject specific toner percentages (e.g., exactly 4%), trigger simultaneous faults, or schedule faults via Web UI. |
| **4. Isolation and Safety** | All testing is confined strictly to the virtual testbed without risk to host or production environments. | Fault injection actions (e.g., service stops, registry changes) are isolated within the VMs and cannot leak into host OS. |
| **5. Portability** | The entire system can run self-contained on a standard demonstration laptop. | Host environment and Windows 11 VM can run locally on modern virtualization software (VirtualBox / VMware / Hyper-V) without internet access. |
| **6. Observability** | All system states, faults, and communication flows are visibly exposed in real time. | Web Control Interface displays live telemetry; all SNMP traps and state transitions are recorded in structured JSON logs. |
| **7. Extensibility** | Modular design allowing straightforward addition of new printer models, MIBs, and fault types. | New fault definitions can be added via modular plugins or config files without modifying core engine logic. |

---

## 5. Team 04 Project Structure

- **Course:** SCI 700 / SCI 701 (UniSC)
- **Team Size:** 2 Members
- **Lead Developer & Systems Architect:** Sukanta Debnath ([@sdPrang0n](https://github.com/sdPrang0n))
- **Endpoint & Interface Developer:** Team Member 2
