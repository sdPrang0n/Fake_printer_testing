# 📋 Project Kanban Board

> **Project:** Fake Printer for Testing Event Management and AI Support Application  
> **Course:** SCI 700 / SCI 701  
> **The Goal:** Build a safe virtual printer and computer troubleshooting environment on a Debian/Ubuntu host and Windows 11 VM to safely and repeatably demonstrate an AI-powered IT support platform.  
> **Tags:** `SNMP` | `Simulation` | `Windows`  
> **Timeline:** 12-Week Iterative Project  
> **🔗 Live GitHub Board:** [https://github.com/users/sdPrang0n/projects/1](https://github.com/users/sdPrang0n/projects/1)  
> **Current Status:** 🟡 **Week 2 (In Progress)**

---

## 👥 Project Team (Team 04 - 2 Members)

| Member | GitHub Handle | Charter Role | Primary Deliverables |
| :--- | :--- | :--- | :--- |
| **Sukanta Debnath** | [@sdPrang0n](https://github.com/sdPrang0n) | Lead Developer & Systems Architect | Simulation Host (Debian/Ubuntu), Virtual Printer Device, SNMP Agent & Trap Generator, Reset/Restore Mechanism |
| **Team Member 2** | *(TBD)* | Endpoint & Interface Developer | Windows 11 Endpoint Fault Agent, Scenario Engine, Web Control Interface, State Monitoring & Logging |

---

## 📌 Board Status

| 📋 To Do (Backlog) | ⚙️ In Progress (Week 2) | ✅ Done (Week 1) |
| :--- | :--- | :--- |
| **Phase 1: Architecture (Week 3)**<br>• System architecture design & VM topology (Debian/Ubuntu Host + Windows 11 VM)<br>• Component communication & event bus interfaces<br><br>**Phase 2: Emulation & Agents (Weeks 4–6)**<br>• Virtual Printer core listener (Port 9100 / IPP)<br>• SNMP Agent implementation (RFC 3805 Printer MIB)<br>• SNMP Trap Generator (asynchronous trap/inform dispatcher)<br>• Windows 11 Endpoint Fault Agent (controlling key services like `spoolsv.exe`)<br>• State monitoring & logging service<br><br>**Phase 3: Scenario & Control UI (Weeks 7–9)**<br>• Scenario Engine (scriptable test cases for AI support demos)<br>• Reset and Restore Mechanism (1-click clean baseline restore)<br>• Web Control Interface (controlling errors and execution timing)<br><br>**Phase 4: AI Integration & Deployment (Weeks 10–12)**<br>• AI IT-support tool demo validation suite<br>• Verification against 7 Core Requirements (Repeatability, Realism, Controllability, Isolation, Portability, Observability, Extensibility)<br>• Deployment and Operating Guide & release package | **Week 2: Fault Library, SNMP Traps & Windows Agent Specs**<br>• Define Printer Fault Library ([FAULT_LIBRARY.md](FAULT_LIBRARY.md)): bad network, toner levels, paper tray status, print cover open<br>• Define SNMP MIB OID mappings & SNMP Trap specifications<br>• Define Windows 11 Endpoint Fault Library (Print Spooler stopped/crashed, stuck queue, driver & port issues)<br>• Specify Reset and Restore procedures for host, printer, and Windows VM | • Git repository initialization<br>• Project definition & requirements specification ([REQUIREMENTS.md](REQUIREMENTS.md))<br>• 12-Week roadmap & deliverable grid finalized<br>• Linked GitHub Project #1 to repository |

---

## 🗓️ 12-Week Feature Roadmap & Tracking

### 🔹 Phase 1: Foundation & Specifications (Weeks 1–3)
- [x] **Week 1:** Project initialization, requirements gathering, and GitHub Kanban board setup. *(Completed)*
- [ ] **Week 2:** Fault Library, SNMP Trap Specifications & Windows Endpoint Faults ([FAULT_LIBRARY.md](FAULT_LIBRARY.md)) — Bad network, toner levels, paper tray status, print cover open, SNMP traps, and Windows 11 service stops. *(CURRENT - IN PROGRESS)*
- [ ] **Week 3:** System Architecture Design, VM Topology & Component Interface Specifications (Debian/Ubuntu Host, Windows 11 VM, Web UI, Scenario Engine).

### 🔹 Phase 2: Emulation, SNMP & Endpoint Agent (Weeks 4–6)
- [ ] **Week 4:** Virtual Printer device core (TCP 9100 / IPP) & SNMP Agent implementation on Debian/Ubuntu VM.
- [ ] **Week 5:** SNMP Trap Generator & Windows 11 Endpoint Fault Agent (spooler stop/crash, queue jam, driver corruption).
- [ ] **Week 6:** State Monitoring & Logging service, integrating real-time telemetry across printer and Windows VM.

### 🔹 Phase 3: Scenario Engine, Reset & Web Control Interface (Weeks 7–9)
- [ ] **Week 7:** Scenario Engine (automated multi-step test case runner for AI IT-support platform demos).
- [ ] **Week 8:** Reset and Restore Mechanism (automated rollback of VM, spooler, and printer to clean baseline).
- [ ] **Week 9:** Web Control Interface (interactive web UI to control errors, trigger faults, and schedule scenarios).

### 🔹 Phase 4: AI Platform Integration, Testing & Deployment (Weeks 10–12)
- [ ] **Week 10:** AI IT-support tool integration and automated evaluation test harness.
- [ ] **Week 11:** End-to-end validation across the 7 Core Requirements (Repeatability, Realism, Controllability, Isolation, Portability, Observability, Extensibility).
- [ ] **Week 12:** Deployment and Operating guide, demonstration execution, and project release.
