# 📋 Project Kanban Board

> **Project 04:** Fake Printer for Testing  
> **The Goal:** Testing an AI IT-support tool on real devices is risky and hard to repeat. Build a safe virtual printer and PC that can break on purpose and be reset.  
> **Tags:** `SNMP` | `Simulation` | `Windows`  
> **Timeline:** 12-Week Iterative Project  
> **🔗 Live GitHub Board:** [https://github.com/users/sdPrang0n/projects/1](https://github.com/users/sdPrang0n/projects/1)  
> **Current Status:** 🟡 **Week 2 (In Progress)**

---

## 👥 Project Team & Roles

| Member | GitHub Handle | Project Role | Primary Deliverables |
| :--- | :--- | :--- | :--- |
| **Sukanta Debnath** | [@sdPrang0n](https://github.com/sdPrang0n) | Project Lead / Core Developer | Virtual Printer Architecture & Planning |
| *Team Member 2* | *(Pending)* | Windows Agent Developer | Windows Print Spooler & Driver Faults |
| *Team Member 3* | *(Pending)* | Simulation & SNMP Specialist | SNMP Printer MIB & Protocol Emulation |
| *Team Member 4* | *(Pending)* | QA & Scenario Engineer | Scenario Engine, Reset/Restore & Testing |

---

## 📌 Board Status

| 📋 To Do (Backlog) | ⚙️ In Progress (Week 2) | ✅ Done (Week 1) |
| :--- | :--- | :--- |
| **Phase 1: Architecture (Week 3)**<br>• System architecture design & component interfaces<br>• Communication protocol between Web UI, Scenario Engine, Printer & Windows Agent<br><br>**Phase 2: Emulation & Agents (Weeks 4–6)**<br>• Virtual printer socket & SNMP agent (RFC 3805 Printer MIB)<br>• Windows Fault Agent (spooler, driver, and queue faults)<br>• Fault injection engine & API integration<br><br>**Phase 3: Scenario & Control (Weeks 7–9)**<br>• Scenario engine (scriptable test cases for AI support tool)<br>• 1-Click Reset and Restore subsystem<br>• Web control interface & monitoring dashboard<br><br>**Phase 4: AI Testing & Release (Weeks 10–12)**<br>• AI IT-support tool test evaluation suite<br>• End-to-end scenario validation & repeatability testing<br>• Final documentation & project release | **Week 2: Fault Library & Error Taxonomy**<br>• Define complete Fault Library ([FAULT_LIBRARY.md](FAULT_LIBRARY.md))<br>• Specify Virtual Printer faults (Paper jam, low toner, door open, offline, corrupt stream)<br>• Specify SNMP MIB OID mapping (`hrPrinterDetectedErrorState`)<br>• Specify Windows PC faults (Spooler stopped/crashed, stuck queue, driver error, port mismatch)<br>• Specify 1-Click Reset & Restore procedures | • Git repository initialization<br>• Project definition & requirements specification<br>• 12-Week roadmap finalized<br>• Linked GitHub Project #1 to repository |

---

## 🗓️ 12-Week Feature Roadmap & Tracking

### 🔹 Phase 1: Foundation & Specifications (Weeks 1–3)
- [x] **Week 1:** Project initialization, requirements gathering, and GitHub Kanban board setup. *(Completed)*
- [ ] **Week 2:** Fault Library & Simulation Specifications ([FAULT_LIBRARY.md](FAULT_LIBRARY.md)) — Virtual printer faults, SNMP OID mappings, Windows spooler faults, and Reset/Restore definitions. *(CURRENT - IN PROGRESS)*
- [ ] **Week 3:** System Architecture Design & Component Interface Specifications (Web UI, Scenario Engine, Virtual Printer, Windows Agent).

### 🔹 Phase 2: Emulation & Windows Fault Agent (Weeks 4–6)
- [ ] **Week 4:** Virtual Printer core listener (Port 9100) and simulated SNMP agent (Port 161).
- [ ] **Week 5:** Windows Fault Agent (simulating spooler service stop, queue jams, driver corruption, and offline state).
- [ ] **Week 6:** Fault Injection Engine (exposing API triggers for each fault in the library).

### 🔹 Phase 3: Scenario Engine & Control Subsystem (Weeks 7–9)
- [ ] **Week 7:** Scenario Engine (automated multi-step test case runner for AI IT-support tool).
- [ ] **Week 8:** Reset and Restore Subsystem (automated rollback of printer, spooler, and queue to clean baseline).
- [ ] **Week 9:** Web Control Interface (interactive web UI to monitor status, trigger faults, and run scenarios).

### 🔹 Phase 4: AI Evaluation, Testing & Final Review (Weeks 10–12)
- [ ] **Week 10:** AI IT-support tool integration and evaluation benchmark suite.
- [ ] **Week 11:** End-to-end test execution, scenario reproducibility, and edge-case validation.
- [ ] **Week 12:** Project review, final demonstration, and project handover.
