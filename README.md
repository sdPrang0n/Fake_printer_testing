# Fake Printer for Testing Event Management and AI Support Application

[![Course](https://img.shields.io/badge/Course-SCI700%20%2F%20SCI701-blue)](https://github.com/sdPrang0n/Fake_printer_testing)
[![Tags](https://img.shields.io/badge/Tags-SNMP%20%7C%20Simulation%20%7C%20Windows-blue)](https://github.com/sdPrang0n/Fake_printer_testing)
[![Project Board](https://img.shields.io/badge/Kanban-GitHub%20Project%20%231-brightgreen)](https://github.com/users/sdPrang0n/projects/1)
[![Current Status](https://img.shields.io/badge/Status-Week%202%20(In%20Progress)-orange)](KANBAN.md)

---

## 📌 Project Overview
This project aims to design and develop a **simulated printer and computer troubleshooting environment** that can be used to demonstrate how an **AI-powered IT support platform** identifies and resolves technical problems.

The customer already has an AI support platform that can diagnose common IT issues on end-users' computers without a service desk agent having to contact the customer. However, demonstrating its capabilities is difficult because intentionally creating problems on real computers and printers can be risky and difficult to repeat. 

The proposed solution creates a virtual testing environment where technical problems can be **simulated, monitored, and resolved** without affecting real devices.

---

## 💼 Customer Problem Statement

> *"I sell an AI Support platform that can help diagnose known issues on end users' computers without a service desk agent having to contact the customer.*
>
> *The biggest issue that I have when doing a demo with the product is that there is often no way to show the system actually fixing a problem as there is no way to 'Break' a live system in a repeatable method.*
>
> *The solutions would involve:*
> - *Creation of a Debian/Ubuntu virtual machine as host.*
> - *Create an SNMP generator that will throw errors as needed.*
> - *Create a fake printer that can report bad network, toner levels, paper tray status, print cover open etc.*
> - *Create a process where key services on a demo virtual machine (Windows 11) are stopped to simulate an issue with the machine. (Print spooler, etc.)*
> - *A web interface to control errors and when they occur."*

---

## 📦 Project Deliverables

The project deliverables are organized into a modular 12-component architecture:

| Component 1 | Component 2 | Component 3 | Component 4 |
| :--- | :--- | :--- | :--- |
| **Simulation Host Environment**<br>Debian / Ubuntu VM hosting the core simulation services. | **Virtual Printer Device**<br>Simulated network printer device accepting print streams (Port 9100 / IPP). | **SNMP Agent & Printer MIB Implementation**<br>Responds to queries with standard Printer MIB (`RFC 3805` / `RFC 1759`) & Host Resources MIB (`RFC 2790`). | **Printer Fault Library**<br>Configurable faults: bad network, toner levels, paper tray status, print cover open, etc. |
| **SNMP Trap Generator**<br>Proactive event generator transmitting asynchronous SNMP traps/informs to event management tools. | **Windows Endpoint Fault Agent**<br>Agent deployed on demo Windows 11 VM to manipulate client-side system states. | **Endpoint Fault Library**<br>Simulates stopped/crashed Print Spooler (`spoolsv.exe`), stuck queues, driver & port errors. | **Reset and Restore Mechanism**<br>One-click baseline recovery mechanism to return host, printer, and PC to a clean state. |
| **Web Control Interface**<br>Interactive web UI to control faults, configure timing, trigger scenarios, and view live status. | **Scenario Engine**<br>Automated test case runner orchestrating multi-step incident workflows for AI tool evaluation. | **State Monitoring and Logging**<br>Real-time telemetry, structured event logging, and state inspection across all components. | **Deployment and Operating Documentation**<br>Complete setup scripts, VM deployment templates, and user/operator guide. |

---

## 🎯 Core Project Requirements

The system is engineered against seven foundational technical criteria:

1. **Repeatability:** Scenarios and injected faults produce identical symptoms and recovery behaviors every time they run.
2. **Realism:** Network packets (TCP 9100), SNMP OIDs, Windows Event Logs, and service behaviors precisely match physical devices and production Windows 11 systems.
3. **Controllability:** Operators can trigger specific faults on-demand, adjust error parameters, and schedule sequential fault timelines via the Web UI or Scenario Engine.
4. **Isolation and Safety:** All fault injection and simulation remain strictly isolated to the virtual testbed, preventing collateral damage to host or network infrastructure.
5. **Portability:** Containerized or VM-based deployment (Debian/Ubuntu host + Windows 11 VM) easily spun up on any developer workstation or demo laptop.
6. **Observability:** Complete visibility into printer status, SNMP events, endpoint agent health, and logs through centralized monitoring.
7. **Extensibility:** Modular architecture enabling rapid addition of new printer models, SNMP traps, and endpoint fault types.

---

## 🗓️ 12-Week Roadmap Overview

- **Phase 1: Foundation & Specifications (Weeks 1–3)**
  - Week 1: Project definition, requirements & GitHub Kanban board setup *(Completed)*
  - **Week 2: Fault Library Specification, SNMP Trap Taxonomy & Windows PC Faults *(Current - In Progress)***
  - Week 3: System architecture design, VM environment topology & component interface definitions
- **Phase 2: Emulation & Agents (Weeks 4–6)**
  - Week 4: Virtual Printer core (Port 9100) & SNMP Agent implementation on Debian/Ubuntu VM
  - Week 5: SNMP Trap Generator & Windows 11 Endpoint Fault Agent (spooler & queue injection)
  - Week 6: State monitoring, structured logging & initial fault library integration
- **Phase 3: Scenario Engine, Control UI & Reset Subsystem (Weeks 7–9)**
  - Week 7: Scenario Engine (scriptable test cases for demoing the AI IT-support tool)
  - Week 8: Reset and Restore subsystem (automated clean state recovery for VM, spooler, and printer)
  - Week 9: Web Control Interface (browser dashboard to trigger errors and view real-time status)
- **Phase 4: AI Platform Integration, Testing & Deployment (Weeks 10–12)**
  - Week 10: AI IT-support tool integration & automated scenario validation suite
  - Week 11: End-to-end testing across all 7 core requirements (Repeatability, Realism, Controllability)
  - Week 12: Deployment and Operating Documentation, final demonstration, and project release

---

## 👥 Project Team & Supervision (Team 04)

- **Project Supervisor:** **Isuru** (Course / Academic Supervisor)

| Member | Charter Role | Primary Focus Area |
| :--- | :--- | :--- |
| **Sukanta Debnath** ([@sdPrang0n](https://github.com/sdPrang0n)) | **Lead Developer & Systems Architect** | Simulation Host (Debian/Ubuntu), Virtual Printer Device, SNMP Agent & Trap Generator, Reset & Restore Subsystem |
| **Team Member 2** | **Endpoint & Interface Developer** | Windows 11 Endpoint Fault Agent, Scenario Engine, Web Control Interface, State Monitoring & QA |

---

## 📊 Project Documents & Kanban

- 🚀 **Live Interactive Board:** [GitHub Project #1](https://github.com/users/sdPrang0n/projects/1)
- 📝 **Task 1A Project Proposal (Individual):** [PROPOSAL_TASK_1A.md](PROPOSAL_TASK_1A.md) | Word Doc: [`docs/Sukanta_Debnath_Task_1A_Proposal.docx`](docs/Sukanta_Debnath_Task_1A_Proposal.docx)
- 📔 **Task 1A Initial Journal Guide:** [docs/JOURNAL_TASK_1A.md](docs/JOURNAL_TASK_1A.md)
- 📋 **System Requirements Specification (SRS):** [REQUIREMENTS.md](REQUIREMENTS.md)
- 📄 **Offline Markdown Board:** [KANBAN.md](KANBAN.md)
- 📜 **Team Charter:** [TEAM_CHARTER.md](TEAM_CHARTER.md) | Word Doc: [`docs/Team_Charter_Team04.docx`](docs/Team_Charter_Team04.docx)
- 📖 **Fault Library Specification:** [FAULT_LIBRARY.md](FAULT_LIBRARY.md)
