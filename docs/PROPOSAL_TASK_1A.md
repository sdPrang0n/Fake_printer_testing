# Project Proposal: Fake Printer for Testing Event Management and AI Support Application

**Course:** SCI 700 — Masters Project / Capstone  
**Institution:** School of Science, Technology and Engineering, University of the Sunshine Coast (UniSC)  
**Task:** Task 1A — Initial Project Proposal (Individual Submission)  
**Student Name:** Sukanta Debnath  
**Student ID / GitHub:** [@sdPrang0n](https://github.com/sdPrang0n)  
**Project Group:** Team 04 (Lead Developer & Systems Architect)  
**Academic Supervisor:** Isuru  
**Date:** November 24, 2026  

---

## 1. Background and Business/Technical Problem

### 1.1 Organizational and Industry Context
Enterprise IT Service Management (ITSM) is experiencing an aggressive transition toward autonomous Tier-1 support automation, driven by artificial intelligence and machine learning (Axelos, 2019). The client commercializes an AI Support Platform engineered to proactively identify, diagnose, and resolve technical issues on end-user endpoints. By intercepting device telemetry and operating system logs, the platform executes self-healing scripts without requiring service desk intervention.

### 1.2 The Core Problem
During commercial sales demonstrations and client proof-of-concept (PoC) evaluations, sales engineers face an operational dilemma: there is currently no safe or repeatable method to demonstrate the AI platform resolving technical failures in real time. Inducing live faults on production client laptops or physical office printers introduces severe liabilities:
1. **Operational Risk and Instability:** Deliberately crashing operating system services, corrupting print drivers, or severing network ports on physical computers risks unrecoverable operating system corruption, data loss, or blue-screen crashes during a customer pitch.
2. **Consumables and Maintenance Overhead:** Physical printer hardware consumes expensive supplies (paper reams, toner cartridges) and suffers mechanical component wear (e.g., roller fatigue during forced paper jams).
3. **Absence of Deterministic Repeatability:** Physical hardware failures are non-deterministic. A sales engineer cannot reliably command a physical printer to jam precisely two minutes into a 30-minute demonstration, nor can they deterministically restore the hardware to a clean baseline within seconds before the next client meeting.

### 1.3 Project Assumptions and Environmental Constraints
- **Assumptions:** The customer's AI Support Platform inspects endpoints using standard enterprise monitoring protocols—specifically SNMP for network peripherals and native Win32/WMI instrumentation for Windows client services.
- **Constraints:** The entire troubleshooting sandbox must operate with strict isolation on a standard demonstration laptop using local virtualization (Debian/Ubuntu host and Windows 11 demo VM). It must have zero reliance on external cloud services or physical consumables, ensuring complete portability in offline settings.

---

## 2. Stakeholder and Client Analysis

A comprehensive stakeholder analysis was conducted to establish communication protocols, govern expectations, and balance technical feasibility against business impact.

```
Stakeholder Power / Interest Matrix:
┌─────────────────────────────────┬─────────────────────────────────┐
│       HIGH POWER / LOW INTEREST │      HIGH POWER / HIGH INTEREST │
│                                 │                                 │
│  • Academic Supervisor (Isuru)  │  • Client / Product Vendor      │
│    (Academic Standards & Rubric)│    (Sales Demo & PoC Teams)     │
├─────────────────────────────────┼─────────────────────────────────┤
│        LOW POWER / LOW INTEREST │       LOW POWER / HIGH INTEREST │
│                                 │                                 │
│  • General University Cohort    │  • Prospective Enterprise Buyers│
│                                 │  • Student Engineering Team     │
│                                 │    (Sukanta Debnath & Partner)  │
└─────────────────────────────────┴─────────────────────────────────┘
```

### 2.1 Stakeholder Profiles and Expectations

| Stakeholder Group | Role & Primary Interest | Operational Expectations | Communication Needs & Governance |
| :--- | :--- | :--- | :--- |
| **Client / Product Vendor** | Product Owner & Commercial Sponsor | Needs a compelling, 100% reliable demo testbed that eliminates sales demonstration failure risks and proves the AI tool's self-healing capabilities. | Bi-weekly technical review syncs; milestone sign-offs; demonstration video walkthroughs. |
| **Prospective Enterprise Buyers** | Enterprise IT Directors, Service Desk Managers | Need empirical, verifiable proof that the AI platform detects genuine enterprise telemetry (RFC 3805 SNMP OIDs, Windows Event Logs) rather than canned mock scripts. | Real-time observability through visual Web UI and clear, auditable system telemetry. |
| **Academic Supervisor (Isuru)** | University Course / Project Supervisor | Ensures the project demonstrates AQF Level 9 engineering rigor, professional governance, adherence to academic integrity, and systematic risk management. | Fortnightly supervisor check-ins; GitHub project auditability; formal milestone submissions. |
| **Project Engineering Team (Team 04)** | Sukanta Debnath (Lead Developer) & Partner | Accountable for designing, implementing, and validating the 12 deliverables within the 12-week schedule. | Daily asynchronous communication via Microsoft Teams; GitHub Project #1 Kanban tracking. |

### 2.2 Communication Governance
To maintain governance, the team adheres to a formal Team Charter. All asynchronous communication, architectural debate, and blocker reporting occur on **Microsoft Teams** with an agreed 24-hour response turnaround. Sprint backlogs and task ownership are tracked transparently on **GitHub Project Board #1**. In the event of a technical deadlock between the two engineering members, the matter is formally escalated to Project Supervisor **Isuru** for mediation.

---

## 3. Objectives, Scope and Exclusions

### 3.1 Project Objectives (SMART)
1. **Specific:** Engineer an isolated two-tier virtual simulation environment (Debian/Ubuntu host + Windows 11 VM) featuring an emulated network printer, an SNMP agent, an active trap dispatcher, a Windows fault agent, and a web control interface.
2. **Measurable:** Implement a Fault Library comprising four printer hardware faults (bad network, toner levels, paper tray, cover open) and six Windows endpoint service faults (spooler stop/crash, queue jams, driver/port misconfigurations) validated by test assertions.
3. **Achievable:** Deploy a 1-click Reset and Restore mechanism returning the virtual printer and Windows print spooler to a clean baseline within five seconds.
4. **Relevant:** Satisfy all seven Core Project Requirements mandated by the client: *Repeatability, Realism, Controllability, Isolation & Safety, Portability, Observability, and Extensibility*.
5. **Time-Bound:** Complete engineering design, implementation, evaluation, and documentation within the 12-week semester.

### 3.2 In-Scope Deliverables
The project scope encompasses twelve deliverables:
- **Core Simulation:** Debian/Ubuntu Simulation Host; Virtual Printer Device on TCP port 9100 and IPP; SNMP Agent implementing RFC 3805 and RFC 2790 MIBs.
- **Fault Generation:** Printer Fault Library (network drop, toner, paper jams, cover open); SNMP Trap Generator; Windows Endpoint Fault Agent; Endpoint Fault Library targeting the Print Spooler (`spoolsv.exe`), drivers, and queues.
- **Control & Operations:** Web Control Interface with interactive fault toggles; Scenario Engine for incident orchestration; State Monitoring and Logging; 1-click Reset and Restore subsystem; Deployment and Operating Documentation.

### 3.3 Scope Exclusions (Managing Scope Creep)
To protect feasibility and prevent scope creep, boundaries are strictly enforced:
- **No Modification of AI Platform:** The team will not modify or retrain the client's proprietary AI Support Platform codebase; the testbed provides external telemetry only.
- **No Physical Hardware:** No physical microcontrollers, circuits, or printer peripherals will be built.
- **Exclusion of Non-Windows Endpoints:** The endpoint agent targets Windows 11 exclusively; macOS and Linux endpoints are out of scope.
- **No Public Cloud Dependencies:** Excludes external cloud hosting; all networking is contained within an offline, host-only virtual subnet.

---

## 4. Deliverables and Acceptance Criteria

The twelve project deliverables represent the tangible outputs of the Statement of Work (SOW). Each deliverable is governed by explicit, testable acceptance criteria aligned with the project's quality standards.

```
System Delivery Workflow:
┌──────────────────────────────┐     ┌──────────────────────────────┐     ┌──────────────────────────────┐
│  Phase 1: Specs & Design     │ ──► │  Phase 2: Core Emulation     │ ──► │  Phase 3: Scenarios & UI     │
│  • Requirements (SRS)        │     │  • Virtual Printer (Port 9100)│    │  • Scenario Engine           │
│  • Fault Library Specs       │     │  • SNMP Agent & Traps        │     │  • Web Control Interface     │
│  • Architecture Design       │     │  • Windows 11 Spooler Agent  │     │  • 1-Click Reset / Restore   │
└──────────────────────────────┘     └──────────────────────────────┘     └──────────────────────────────┘
```

| Deliverable | Handover Format | Acceptance & Quality Criteria |
| :--- | :--- | :--- |
| **1. Simulation Host Environment** | VirtualBox / VMware VM appliance (Debian 12 / Ubuntu 22.04 LTS) | Clean headless Linux environment booting in under 45 seconds with pre-configured network bridge to Windows 11 VM. |
| **2. Virtual Printer Device** | Python socket service listening on TCP port 9100 / IPP | Successfully accepts, buffers, and acknowledges raw print data streams without socket crashes or memory leaks. |
| **3. SNMP Agent & Printer MIB** | Net-SNMP / Python daemon on UDP port 161 | Fully responds to standard SNMP `GET` and `WALK` requests for RFC 3805 (`prtMarkerSuppliesLevel`, `hrPrinterDetectedErrorState`). |
| **4. Printer Fault Library** | Modular Python fault modules | Deterministically triggers bad network (packet loss), low/empty toner, paper tray jams, and open cover flags upon invocation. |
| **5. SNMP Trap Generator** | Python asynchronous UDP 162 transmitter | Dispatches valid SNMPv2c traps containing enterprise OIDs and varbind payloads matching triggered fault conditions. |
| **6. Windows Endpoint Fault Agent** | Background Windows service (PowerShell / Win32 API) | Executes on Windows 11 with administrative privileges, executing remote command instructions from the Simulation Host. |
| **7. Endpoint Fault Library** | Scriptable fault execution library | Successfully stops or crashes `spoolsv.exe`, locks corrupted `.SPL`/`.SHD` files in `C:\Windows\System32\spool\PRINTERS`, and toggles offline mode. |
| **8. Reset and Restore Mechanism** | Automated shell / RPC script | Restores printer buffers, clears SNMP fault OIDs, restarts Windows Spooler, purges queue files, and restores online state in **< 5 seconds**. |
| **9. Web Control Interface** | Responsive browser dashboard (HTML5 / CSS / FastAPI) | Provides 1-click buttons for fault injection, error scheduling controls, and real-time status cards reflecting printer/PC health. |
| **10. Scenario Engine** | JSON/YAML test runner engine | Executes automated multi-step incident workflows (e.g., inject fault ➔ send trap ➔ verify resolution) with deterministic reproducibility across 20 cycles. |
| **11. State Monitoring and Logging** | Centralized structured JSON audit log | Captures all state transitions, client connections, SNMP traps, and reset actions with millisecond timestamps. |
| **12. Deployment & Operating Documentation** | Comprehensive PDF/Markdown guide | Enables an independent technical user to deploy, configure, and execute the full testbed on a clean host machine in under 30 minutes. |

---

## 5. Value Proposition

The proposed testing platform delivers substantial commercial, operational, and technical value to the client organization:

```
Value Creation Triangle:
                  ▲ Commercial Impact
                 / \ • 100% Demo Reliability
                /   \ • Shortened Enterprise Sales Cycles
               /     \ • Verifiable AI Capabilities
              /───────\
             /         \
            /           \ Operational & Technical Impact
           /             \ • Zero Hardware Consumables Cost
          /               \ • Deterministic CI Benchmarking
         └─────────────────┘ • Complete Sandbox Safety
```

1. **Commercial Value (Unlocking Sales Acceleration):** In enterprise software sales, seeing is believing. By replacing static slide decks with live, interactive problem-resolution demonstrations, sales engineers can tangibly prove the AI platform's autonomous troubleshooting value. This directly mitigates buyer skepticism and accelerates sales pipeline velocity.
2. **Operational Value (Zero Consumable Costs & Risk Elimination):** The virtual environment completely eliminates physical consumables expenditure (reams of paper, laser toner cartridges) and removes the risk of physical printer damage. Furthermore, client demonstration laptops remain completely safe from operating system corruption.
3. **Technical and Engineering Value (Standardized AI Benchmarking):** Beyond commercial demonstrations, the testbed provides the client's internal software engineering team with a repeatable, automated Continuous Integration (CI) regression harness. New releases of the AI Support Platform can be benchmarked against standardized, scripted fault scenarios to verify remediation efficacy before commercial deployment.

---

## 6. Solution Idea & Architectural Concept

### 6.1 Architectural Topology
The proposed technical solution is built upon an isolated, two-tier virtualization topology running locally on the demonstration laptop:

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
                           │ (Control RPC)                         │
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

1. **Simulation Host (Debian/Ubuntu VM):** Acts as the central simulation engine. It executes a multi-threaded Python TCP socket server (port 9100) to ingest print traffic, alongside a Python/Net-SNMP daemon exposing RFC 3805 OIDs. An asynchronous trap engine dispatches SNMPv2c traps to the event management interface. The host serves the Web Control Interface (built with FastAPI and responsive HTML5) and runs the Scenario Engine.
2. **Demo Endpoint (Windows 11 VM):** Represents the target end-user workstation. It runs the Windows Endpoint Fault Agent, a background service leveraging native Win32 APIs and PowerShell cmdlets (`Stop-Service`, `Set-Printer`) to execute precise service disruptions on command.
3. **Inter-System Networking:** Both virtual machines communicate across a dedicated host-only virtual switch, completely isolated from corporate Wi-Fi or public networks, ensuring absolute safety and determinism.

### 6.2 Solution Concept Trade-Off Analysis

| Architectural Dimension | Recommended Approach: Dual-VM Simulation | Alternative Approach: Docker Containerized Emulation | Trade-Off Rationale |
| :--- | :--- | :--- | :--- |
| **Windows Service Realism** | High: Full native Windows 11 kernel executing real `spoolsv.exe` and native print drivers. | Low: Windows container support is limited and cannot fully replicate interactive Win32 desktop print subsystems. | A full Windows 11 VM is essential to satisfy the **Realism** core requirement for the client's AI agent. |
| **Resource Utilization** | Moderate: Requires 8–16 GB RAM to execute dual virtual machines comfortably. | Low: Containers consume significantly less RAM and CPU. | Modern demonstration laptops possess 16–32 GB RAM, making VM resource consumption an acceptable trade-off for fidelity. |
| **Isolation & Portability** | High: VM appliances (.OVA/.OVF) can be exported and imported into VirtualBox or VMware workstation in minutes. | High: Docker images are lightweight but require Docker Desktop licensing on corporate Windows hosts. | VM appliances offer superior, license-free portability for client sales staff. |

---

## 7. References

Axelos. (2019). *ITIL Foundation: ITIL 4 Edition*. TSO (The Stationery Office).

Bergman, R., Lewis, H., & McDonald, I. (2004). *Printer MIB v2* (RFC 3805). Internet Engineering Task Force (IETF). https://doi.org/10.17487/RFC3805

Gartner. (2023). *Market Guide for AIOps Platforms*. Gartner Research.

Gruschke, B. (1998). Integrated event management: Event correlation using dependency graphs. *Proceedings of the 9th IFIP/IEEE International Workshop on Distributed Systems: Operations and Management*, 130–141.

Hsueh, M. C., Tsai, T. K., & Iyer, R. K. (1997). Fault injection techniques and tools. *IEEE Computer*, 30(4), 75–82. https://doi.org/10.1109/2.585157

Smith, P., & Wright, J. (2000). *Printer MIB* (RFC 1759). Internet Engineering Task Force (IETF). https://doi.org/10.17487/RFC1759

Waldbusser, S., & Grillo, P. (1999). *Host Resources MIB* (RFC 2790). Internet Engineering Task Force (IETF). https://doi.org/10.17487/RFC2790
