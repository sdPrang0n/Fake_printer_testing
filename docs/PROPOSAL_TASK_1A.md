# Project Proposal: Fake Printer for Testing Event Management and AI Support Application

**Course:** SCI 700 — Masters Project / Capstone  
**Institution:** School of Science, Technology and Engineering, University of the Sunshine Coast (UniSC)  
**Task:** Task 1A — Initial Project Proposal (Individual Submission, AQF Level 9)  
**Student Name:** Sukanta Debnath  
**Student ID / GitHub:** [@sdPrang0n](https://github.com/sdPrang0n)  
**Project Group:** Team 04 (Lead Developer & Systems Architect, 2-Member Team)  
**Academic Supervisor:** Isuru  
**Date:** November 2026  

---

## Executive Overview

**Project Concept (What It Is):** This project delivers an isolated, two-tier virtualization testbed engineered to benchmark, test, and demonstrate enterprise AI IT-support and event management applications. The system emulates an enterprise network printer alongside a Windows 11 endpoint, embedding scriptable fault injectors to replicate hardware, network, and operating system incidents without physical hardware.

**Operational Mechanism (How It Works):** The platform executes an isolated Debian/Ubuntu Simulation Host bridged locally to a Windows 11 client VM. The Linux host runs an emulated print listener (TCP 9100 / IPP), an SNMP daemon serving standard RFC 3805/2790 MIBs, and an asynchronous trap generator. The Windows VM hosts a background agent executing OS-level disruptions, including halting `spoolsv.exe`, locking queue files (`*.SPL`/`*.SHD`), and modifying driver states. A unified Web Control Interface and Scenario Engine orchestrates multi-step failure workflows on demand, while an automated 1-click restore mechanism resets both environments to baseline in under 5 seconds.

**Problem Solved in Short:** Demonstrating autonomous self-healing software during live enterprise sales pitches or CI test cycles is hazardous and unrepeatable on physical machines. Inducing faults on production PCs risks blue-screen crashes, physical printers waste paper and toner, and hardware jams cannot be synchronized or reset quickly. This solution provides a 100% safe, portable, deterministic, and zero-cost virtual demonstration and testing sandbox.

---

## Table of Contents

- [Executive Overview](#executive-overview)
- [1. Background and Business/Technical Problem](#1-background-and-businesstechnical-problem)
  - [1.1 Organizational Context and Problem Statement](#11-organizational-context-and-problem-statement)
  - [1.2 Project Assumptions and Environmental Constraints](#12-project-assumptions-and-environmental-constraints)
- [2. Stakeholder and Client Analysis](#2-stakeholder-and-client-analysis)
  - [2.1 Stakeholder Matrix and Operational Expectations](#21-stakeholder-matrix-and-operational-expectations)
  - [2.2 Team Governance and Communication Protocols](#22-team-governance-and-communication-protocols)
- [3. Objectives, Scope and Exclusions](#3-objectives-scope-and-exclusions)
  - [3.1 SMART Project Objectives](#31-smart-project-objectives)
  - [3.2 In-Scope Deliverables](#32-in-scope-deliverables)
  - [3.3 Scope Exclusions and Boundary Management](#33-scope-exclusions-and-boundary-management)
- [4. Deliverables and Acceptance Criteria](#4-deliverables-and-acceptance-criteria)
- [5. Value Proposition (Commercial, Operational, Technical)](#5-value-proposition)
- [6. Solution Idea & Architectural Concept](#6-solution-idea--architectural-concept)
  - [6.1 Dual-VM Simulation Topology](#61-dual-vm-simulation-topology)
  - [6.2 Architectural Trade-Off Analysis](#62-architectural-trade-off-analysis)
- [7. References (APA 7th Edition)](#7-references)

---

## 1. Background and Business/Technical Problem

### 1.1 Organizational Context and Problem Statement
Modern IT Service Management (ITSM) increasingly relies on AIOps platforms to automate Tier-1 incident resolution (Axelos, 2019). The client commercializes an AI support platform that intercepts endpoint telemetry to remediate device failures. In commercial sales demonstrations and client proof-of-concept evaluations, sales engineers must prove that the AI resolves real-world incidents. However, inducing failures on live infrastructure introduces critical operational liabilities:
- **Operational Risk:** Crashing services, severing network ports, or corrupting drivers on live PCs risks permanent OS corruption and catastrophic blue-screen crashes during client presentations.
- **Consumable Overhead:** Physical printers consume expensive paper and toner, suffering mechanical wear during induced jams.
- **Non-Deterministic Timing:** Physical failures cannot be synchronized to a sales pitch, nor restored within seconds before the next meeting.

### 1.2 Project Assumptions and Environmental Constraints
Key assumptions assume the client's AI platform monitors endpoints using standard protocols: SNMP for network peripherals and Win32/WMI APIs for Windows systems. Environmental constraints dictate that the sandbox must operate in complete isolation on a standard demonstration laptop (16 GB RAM) without cloud dependencies or physical consumables.

---

## 2. Stakeholder and Client Analysis

### 2.1 Stakeholder Matrix and Operational Expectations
A structured stakeholder analysis governs technical alignment and delivery expectations across all parties:

| Stakeholder Group | Core Interest / Role | Operational Expectations |
| :--- | :--- | :--- |
| **Client / Product Vendor** | Commercial Sponsor (Sales & QA) | Needs a reliable demo testbed to prove AI self-healing without demo crash risks. |
| **Enterprise Buyers** | Target Customers (IT Directors) | Requires authentic telemetry (RFC 3805 OIDs, Event Logs) rather than mock scripts. |
| **Academic Supervisor (Isuru)** | Course / Academic Supervisor | Requires AQF Level 9 engineering rigor, professional governance, and risk mitigation. |
| **Engineering Team (Team 04)** | Sukanta Debnath & Partner | Accountable for architecting and delivering all 12 deliverables within 12 weeks. |

### 2.2 Team Governance and Communication Protocols
The project is executed by a two-member team governed by a formal Team Charter. Asynchronous communication occurs via Microsoft Teams with a mandatory 24-hour response turnaround. Sprint backlogs are managed on GitHub Project Board #1. Technical disputes are resolved through consensus; persistent deadlocks escalate to Project Supervisor Isuru.

---

## 3. Objectives, Scope and Exclusions

### 3.1 SMART Project Objectives
1. **Specific:** Engineer an isolated dual-VM testbed (Debian host + Windows 11 client) featuring virtual printing, SNMP agent, trap dispatcher, Windows endpoint agent, and web dashboard.
2. **Measurable:** Implement 4 printer hardware faults and 6 Windows spooler/driver faults verified by automated test assertions.
3. **Achievable:** Deliver a 1-click reset mechanism restoring baseline operating conditions in under 5 seconds.
4. **Relevant:** Fulfill all 7 client requirements: *Repeatability, Realism, Controllability, Isolation, Portability, Observability, Extensibility*.
5. **Time-Bound:** Complete engineering, verification, and documentation within the 12-week semester.

### 3.2 In-Scope Deliverables
Scope comprises 12 deliverables: (1) Debian/Ubuntu Simulation Host, (2) Port 9100/IPP Virtual Printer, (3) RFC 3805 SNMP Agent, (4) Printer Fault Library, (5) SNMP Trap Generator, (6) Windows Endpoint Fault Agent, (7) Windows Fault Library, (8) 1-Click Reset Subsystem, (9) Web Control Interface, (10) Scenario Engine, (11) State Monitoring & Logging, and (12) Deployment Guides.

### 3.3 Scope Exclusions (Managing Scope Creep)
To safeguard schedule feasibility, strict exclusions apply: no modification of the client's proprietary AI code; no physical microcontrollers or circuits; no support for macOS/Linux endpoints; and zero public cloud dependencies.

---

## 4. Deliverables and Acceptance Criteria

The project deliverables represent the tangible outputs of the Statement of Work, governed by rigorous acceptance criteria:

| Deliverable | Handover Format | Acceptance & Quality Criteria |
| :--- | :--- | :--- |
| **1. Simulation Host** | VM Appliance (Debian 12 / Ubuntu) | Boots in < 45s; host-only networking isolated from corporate LAN. |
| **2. Virtual Printer** | Python TCP 9100 / IPP service | Accepts, buffers, and acknowledges raw print streams reliably. |
| **3. SNMP Agent & MIB** | Net-SNMP daemon (UDP 161) | Fully answers GET/WALK requests for RFC 3805 printer supply/error OIDs. |
| **4. Printer Faults** | Modular Python fault engine | Injects network drops, low toner, paper jams, and cover open states. |
| **5. SNMP Trap Generator** | Async UDP 162 dispatcher | Transmits RFC-compliant enterprise traps upon fault state changes. |
| **6. Windows Endpoint Agent** | Background Windows Service | Runs with admin rights on Windows 11; receives remote commands. |
| **7. Endpoint Faults** | PowerShell/Win32 fault library | Stops `spoolsv.exe`, locks `.SPL`/`.SHD` files, and unbinds printer ports. |
| **8. Reset & Restore** | Automated shell/RPC script | Purges queues and restores clean printer/spooler baseline in < 5 seconds. |
| **9. Web Control UI** | FastAPI / HTML5 Dashboard | Interactive fault toggles, execution timers, and real-time health cards. |
| **10. Scenario Engine** | YAML/JSON test runner | Executes multi-step incident chains with 100% deterministic reproducibility. |
| **11. State & Audit Logs** | Structured JSON audit logger | Logs state transitions, client connections, and traps with ms precision. |
| **12. Documentation** | Deployment & Operations Guide | Enables independent fresh deployment on host hardware in < 30 minutes. |

---

## 5. Value Proposition

The solution delivers multi-dimensional value across commercial, operational, and engineering domains:
- **Commercial Impact (Sales Acceleration):** Replaces static slides with live problem-resolution demonstrations. Sales engineers prove autonomous self-healing in real time, overcoming client skepticism and shortening deal cycles.
- **Operational Impact (Zero Overhead & Risk):** Eliminates hardware wear, paper waste, and toner costs while isolating production laptops from OS instability.
- **Technical Impact (Automated CI Benchmarking):** Provides an automated regression test harness allowing engineering teams to benchmark AI diagnostic accuracy against repeatable incident scenarios.

---

## 6. Solution Idea & Architectural Concept

### 6.1 Dual-VM Simulation Topology
The system employs a local dual-VM architecture: a Debian/Ubuntu Simulation Host running the print listener, SNMP engine, FastAPI web interface, and scenario orchestrator; and a Windows 11 VM hosting the endpoint fault agent. Communication flows over an isolated virtual host-only network, guaranteeing offline portability and zero enterprise network interference.

### 6.2 Architectural Trade-Off Analysis

| Dimension | Selected Approach: Dual-VM | Alternative: Docker Containers |
| :--- | :--- | :--- |
| **Realism** | High: Native Windows 11 kernel executing genuine `spoolsv.exe` and print drivers. | Low: Windows containers cannot replicate full interactive desktop spooler subsystem. |
| **Resource Footprint** | Moderate: Requires 8–16 GB RAM for smooth dual-VM execution. | Low: Minimal RAM overhead, but lacks desktop OS fidelity required by AI agent. |
| **Portability** | High: Appliance (.OVA) runs on standard VirtualBox/VMware without licensing fees. | Moderate: Docker Desktop mandates corporate subscription licenses. |

---

## 7. References

Axelos. (2019). *ITIL Foundation: ITIL 4 Edition*. TSO (The Stationery Office).

Bergman, R., Lewis, H., & McDonald, I. (2004). *Printer MIB v2* (RFC 3805). Internet Engineering Task Force (IETF). https://doi.org/10.17487/RFC3805

Gartner. (2023). *Market Guide for AIOps Platforms*. Gartner Research.

Gruschke, B. (1998). Integrated event management: Event correlation using dependency graphs. *Proceedings of the 9th IFIP/IEEE International Workshop on Distributed Systems: Operations and Management*, 130–141.

Hsueh, M. C., Tsai, T K., & Iyer, R. K. (1997). Fault injection techniques and tools. *IEEE Computer*, 30(4), 75–82. https://doi.org/10.1109/2.585157

Smith, P., & Wright, J. (2000). *Printer MIB* (RFC 1759). Internet Engineering Task Force (IETF). https://doi.org/10.17487/RFC1759

Waldbusser, S., & Grillo, P. (1999). *Host Resources MIB* (RFC 2790). Internet Engineering Task Force (IETF). https://doi.org/10.17487/RFC2790
