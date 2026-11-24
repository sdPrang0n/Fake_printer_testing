# 📜 Team Charter — Team 04

| Project Detail | Information |
| :--- | :--- |
| **Team Number** | **Team 04** |
| **Project Title** | **Fake Printer for Testing Event Management and AI Support Application** |
| **Course / Program** | SCI 700 / SCI 701 — University of the Sunshine Coast (UniSC) |
| **Project Repository** | [sdPrang0n/Fake_printer_testing](https://github.com/sdPrang0n/Fake_printer_testing) |
| **Interactive Board** | [GitHub Project #1](https://github.com/users/sdPrang0n/projects/1) |
| **Tags** | `SNMP` \| `Simulation` \| `Windows` |
| **Project Supervisor** | **Isuru** (Course / Academic Supervisor) |
| **Team Size** | **2 Members** |
| **Team Members** | **Sukanta Debnath**, **Team Member 2** |

---

## 1. Purpose

The purpose of Team 04 is to design, develop, and demonstrate a simulated printer and computer troubleshooting environment that can be used to demonstrate how an **AI-powered IT support platform** identifies and resolves technical problems.

The customer already has an AI support platform capable of diagnosing known issues on end users' computers without a service desk agent needing to contact the customer. However, demonstrating its capabilities during sales or evaluation demos is difficult because intentionally creating problems on real production computers and printers is risky and difficult to repeat.

To solve this, Team 04 is engineering a safe, controllable virtual environment comprising:
- **Simulation Host Environment:** A Debian/Ubuntu virtual machine hosting simulation services.
- **Virtual Printer Device:** Emulated network printer responding to print jobs (Port 9100 / IPP).
- **SNMP Agent & Printer MIB Implementation:** Providing standard RFC 3805 / RFC 1759 device status queries.
- **SNMP Trap Generator:** Proactively throwing asynchronous alerts and error traps into enterprise event management platforms.
- **Printer Fault Library:** Simulating bad network conditions, toner levels, paper tray status (jams, out-of-paper), and print cover open states.
- **Windows Endpoint Fault Agent:** Running on a demo Windows 11 VM to manipulate client-side system services.
- **Endpoint Fault Library:** Simulating stopped/crashed Print Spooler (`spoolsv.exe`), jammed queues, and driver/port misconfigurations.
- **Scenario Engine:** Scripted multi-step incident workflows for automated AI platform testing.
- **Web Control Interface:** A browser-based interface to control errors, schedule triggers, and monitor live status.
- **State Monitoring & Logging:** Comprehensive telemetry and structured logging across host, printer, and Windows VM.
- **Reset and Restore Mechanism:** Fast, one-click baseline restoration ensuring complete test repeatability.
- **Deployment and Operating:** Deployment scripts and operational documentation.

All work is guided by the **7 Core Project Requirements**: *Repeatability, Realism, Controllability, Isolation & Safety, Portability, Observability, and Extensibility*.

---

## 2. Decision-Making Process (2-Member Team)

- **Primary Approach (Consensus & Consultation):**  
  Major architectural, technical design, protocol selection, and scope decisions will be made through mutual consensus so both members maintain shared ownership of the technical implementation. Each member will consult the other before finalizing design specifications.

- **Minor Decisions (Command / Ownership):**  
  Routine formatting, minor refactoring, and component-specific code adjustments with low impact can be decided independently by the assigned task owner and communicated during syncs.

- **Contingency Plan for Deadlocks (Supervisor Escalation):**  
  Because the team consists of 2 members, a majority vote is mathematically impossible during a split decision. If a technical or scope disagreement cannot be resolved through consensus within 24 hours, both members agree to document both perspectives and jointly consult the project supervisor (**Isuru**) for final determination.

---

## 3. Roles and Responsibilities

To ensure balanced accountability across a 2-person engineering team, the 12 project deliverables are divided as follows:

| Role Title | Primary Assignee | Core Deliverables & Responsibilities |
| :--- | :--- | :--- |
| **Lead Developer & Systems Architect** | **Sukanta Debnath** | • **Simulation Host Environment:** Setup and configuration of Debian/Ubuntu VM.<br>• **Virtual Printer Device:** Network transport, socket listener (Port 9100), and stream ingestion.<br>• **SNMP Agent & Printer MIB:** Implementing RFC 3805/1759 OIDs for printer status queries.<br>• **SNMP Trap Generator:** Building proactive asynchronous trap/inform dispatcher.<br>• **Printer Fault Library:** Implementing paper jam, toner, cover open, and bad network faults.<br>• **Reset and Restore Mechanism:** Host-side and printer reset automation.<br>• **Project Management:** GitHub repository administration, sprint tracking, and milestone coordination. |
| **Endpoint & Interface Developer** | **Team Member 2** | • **Windows Endpoint Fault Agent:** Service controller on demo Windows 11 VM.<br>• **Endpoint Fault Library:** Simulating stopped/crashed Print Spooler (`spoolsv.exe`), stuck queues, driver/port faults.<br>• **Scenario Engine:** Scriptable test case runner orchestrating multi-step AI support demos.<br>• **Web Control Interface:** Building frontend dashboard for fault triggering and timeline control.<br>• **State Monitoring & Logging:** Aggregating real-time state telemetry and structured audit logs.<br>• **Deployment & Operating:** Writing setup scripts, VM deployment guides, and rubric compliance QA. |

---

## 4. Working Agreements

### 📡 Communication Channels
- **Primary Channel:** **Microsoft Teams** serves as the central hub for all asynchronous messaging, file sharing, quick questions, and virtual calls.
- **Code & Project Tracking:** **GitHub** repository ([`Fake_printer_testing`](https://github.com/sdPrang0n/Fake_printer_testing)) and **GitHub Project Board #1** are used for version control, issue tracking, and sprint tracking.

### ⏱️ Response Time & Availability
- **Response Commitment:** Members agree to check Microsoft Teams regularly and acknowledge messages, pull requests, or blockers within **24 hours**.
- **Meeting Cadence:**
  - **Quick Syncs:** In-person or virtual touchpoints immediately following scheduled classes.
  - **Collaborative Work Sessions:** Virtual Teams calls scheduled on weekends for deeper technical collaboration and sprint reviews.
- **Schedule Changes:** Any work-shift or academic conflict must be flagged in Microsoft Teams at least **24 hours** before a scheduled sync to allow rescheduling.

### 🤝 Accountability & Transparency
- Members will commit code and documentation regularly to maintain visibility.
- Technical blockers or delays must be flagged early in Teams rather than waiting until deadline day.
- Pair programming and code reviews will be conducted for core component integrations.

### ⚖️ Conflict Resolution Process
1. **Direct Inquiry:** Address misunderstandings early by focusing objectively on the code/deliverable rather than the individual, assuming positive intent.
2. **Team Review:** If a disagreement persists, dedicate time during the next Teams sync to openly discuss the issue and adjust task distributions.
3. **Supervisor Mediation:** If internal resolution cannot be reached after a dedicated discussion, jointly reach out to the project supervisor (**Isuru**) for formal guidance and mediation.
