# Project 04: Fake Printer for Testing

[![Tags](https://img.shields.io/badge/Tags-SNMP%20%7C%20Simulation%20%7C%20Windows-blue)](https://github.com/sdPrang0n/Fake_printer_testing)
[![Project Board](https://img.shields.io/badge/Kanban-GitHub%20Project%20%231-brightgreen)](https://github.com/users/sdPrang0n/projects/1)
[![Current Status](https://img.shields.io/badge/Status-Week%202%20(In%20Progress)-orange)](KANBAN.md)

---

## 🎯 The Goal
Testing an **AI IT-support tool** on real devices is risky, expensive, and hard to repeat. 

The objective of this project is to build a safe, controllable **virtual printer and PC environment** that can **break on purpose** (simulate real-world IT printer problems) and be **reliably reset and restored** to clean states for automated, repeatable AI evaluation.

---

## 📦 What You'll Build (Core Deliverables)

1. **Virtual Printer with a Library of Faults**:
   - Emulates a networked printer listening on standard ports (e.g., Raw TCP 9100 / JetDirect).
   - Implements **SNMP** (Simple Network Management Protocol) simulation to report standard printer MIB OIDs (status, paper out, door open, low toner).
   - Fault library to trigger simulated printer issues on-demand.

2. **Windows Fault Agent for PC Problems**:
   - Simulates common client-side printing issues on Windows PCs.
   - Injects faults into the Windows printing subsystem:
     - Print Spooler service stopped or crashed (`spoolsv.exe`).
     - Corrupted, missing, or mismatched printer drivers.
     - Print jobs stuck in the queue (`C:\Windows\System32\spool\PRINTERS`).
     - Port / IP misconfiguration or printer toggled to "Use Printer Offline".

3. **Scenario Engine to Run Test Cases**:
   - Automated orchestration engine to run multi-step IT support test scenarios.
   - Triggers specific sequences of printer and PC faults, waits for the AI IT-support tool to diagnose/remediate, and verifies resolution.

4. **Web Control Interface**:
   - An interactive dashboard for developers and test operators.
   - Allows manual 1-click fault injection, real-time monitoring of printer/PC status, and test scenario execution.

5. **Reset and Restore**:
   - Automated recovery mechanism to restore the virtual printer, Windows print spooler, queues, and drivers back to a clean baseline state after every test.

---

## 🏷️ Technical Scope & Tags
- **SNMP**: Emulating RFC 1759 / RFC 3805 Printer MIB queries (e.g., `hrPrinterStatus`, `hrPrinterDetectedErrorState`).
- **Simulation**: Safe virtualization of printer transport, stream ingestion, and error states without physical hardware.
- **Windows**: Windows Print Spooler management, driver simulation, and client OS fault injection.

---

## 📋 Requirements

### Functional Requirements
- **FR-1: Printer Emulation & Fault Library**: Virtual printer accepts print jobs and exposes controllable fault states (paper jam, out of toner, offline, buffer overflow, corrupt stream).
- **FR-2: SNMP Agent Simulation**: Responds to SNMP `GET` / `WALK` requests with accurate OID values reflecting healthy vs faulted printer states.
- **FR-3: Windows Client Fault Simulation**: Agent capable of altering spooler service state, corrupting queue files, or modifying printer registry/port settings.
- **FR-4: Scenario Orchestration**: Execute automated test cases defining initial state, fault injection sequence, expected AI diagnostic steps, and success criteria.
- **FR-5: Web Management Console**: Web UI for monitoring system status, triggering faults, and managing test scenarios.
- **FR-6: One-Click Reset & Restore**: Complete environment rollback to clean baseline within seconds.

### Non-Functional Requirements
- **NFR-1: Safety & Isolation**: Fault injection strictly isolated to virtual components without damaging host systems.
- **NFR-2: Repeatability**: Scenarios produce identical symptoms and error states across consecutive runs.
- **NFR-3: Extensibility**: Easy addition of new faults to the fault library via modular definitions.
- **NFR-4: Traceability**: All project phases tracked in the Kanban board.

---

## 🗓️ 12-Week Roadmap Overview

- **Phase 1: Foundation & Specifications (Weeks 1–3)**
  - Week 1: Project definition, requirements & Kanban board setup *(Completed)*
  - **Week 2: Fault Library Specification & Windows/SNMP Error Taxonomy *(Current - In Progress)***
  - Week 3: System architecture design & inter-component interface definitions
- **Phase 2: Emulation & Windows Fault Agent (Weeks 4–6)**
  - Week 4: Virtual printer core & SNMP simulation agent
  - Week 5: Windows Fault Agent (spooler, driver, and queue fault injectors)
  - Week 6: Fault injection engine & API integration
- **Phase 3: Scenario Engine & Reset Subsystem (Weeks 7–9)**
  - Week 7: Scenario engine (test case runner and workflow sequencer)
  - Week 8: Reset and restore subsystem (automated clean state recovery)
  - Week 9: Web control interface (dashboard for faults, status, and scenarios)
- **Phase 4: AI Integration, Testing & Delivery (Weeks 10–12)**
  - Week 10: AI IT-support tool integration & evaluation test suite
  - Week 11: End-to-end scenario validation and repeatability verification
  - Week 12: Project review, final documentation, and release

---

## 👥 Project Team (Team 04)

| Member | Charter Role | Focus Area |
| :--- | :--- | :--- |
| **Sukanta Debnath** ([@sdPrang0n](https://github.com/sdPrang0n)) | Facilitator & Lead Developer | Virtual Printer Backend, TCP 9100 Listener & SNMP Emulation |
| **Rejoana Carol** | Strategist & QA / Testing Lead | Test Cases, Fault Validation Runs & Rubric Criteria |
| **Kanijfatma Arifali Tharadara** | Recorder & Spokesperson (UI / Docs) | Web Control Interface, Documentation & Presentation Materials |

---

## 📊 Project Documents & Kanban

- 🚀 **Live Interactive Board:** [GitHub Project #1](https://github.com/users/sdPrang0n/projects/1)
- 📄 **Offline Markdown Board:** [KANBAN.md](KANBAN.md)
- 📜 **Team Charter:** [TEAM_CHARTER.md](TEAM_CHARTER.md) | Word Doc: [`Team_Charter_Team04.docx`](Team_Charter_Team04.docx)
- 📖 **Fault Library Specification:** [FAULT_LIBRARY.md](FAULT_LIBRARY.md)
