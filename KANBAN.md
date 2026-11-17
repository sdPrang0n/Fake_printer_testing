# 📋 Project Kanban Board

> **Project:** Virtual Printer Error Detection System  
> **Timeline:** 12-Week Iterative Project  
> **Scope:** Emulating virtual printing, capturing print jobs, and detecting printing errors one feature at a time.  
> **🔗 Live GitHub Board:** [https://github.com/users/sdPrang0n/projects/1](https://github.com/users/sdPrang0n/projects/1)

---

## 👥 Project Team & Roles

| Member | GitHub Handle | Project Role | Primary Focus |
| :--- | :--- | :--- | :--- |
| **Sukanta Debnath** | [@sdPrang0n](https://github.com/sdPrang0n) | Project Lead / Core Developer | Virtual Printer Architecture & Planning |
| *Team Member 2* | *(Pending)* | Developer / Protocol Specialist | Stream Buffering & Error Injection |
| *Team Member 3* | *(Pending)* | Error Detection Specialist | Syntax Validation & Network Faults |
| *Team Member 4* | *(Pending)* | QA & Diagnostics Lead | Testing, Error Reporting & Logging |

*(Provide names/usernames to update these assignments)*

---

## 📌 Board Status

| 📋 To Do (Backlog) | ⚙️ In Progress | ✅ Done |
| :--- | :--- | :--- |
| **Phase 1: Foundation (Week 3)**<br>• Document protocol specifications (Raw TCP / ESC-POS / Text)<br>• System architecture design & component interfaces<br><br>**Phase 2: Emulation & Capture (Weeks 4–6)**<br>• Virtual printer socket interface<br>• Payload stream buffering & raw storage<br>• Connection state & lifecycle tracking<br><br>**Phase 3: Error Detection (Weeks 7–9)**<br>• Syntax & command byte validator<br>• Connection drops & timeout detector<br>• Payload truncation & corruption detector<br>• Simulated hardware error states (offline, out-of-paper)<br><br>**Phase 4: Diagnostics & Release (Weeks 10–12)**<br>• Structured error reporting & diagnostic logs<br>• Automated test suite & error injection suite<br>• Final documentation & release package | **Week 2: Error Taxonomy & Rules**<br>• Finalize error classification taxonomy<br>• Define error detection schemas and test thresholds | • Git repository initialization<br>• Project definition & objectives documented<br>• Requirements specification established<br>• 12-Week roadmap finalized<br>• Linked GitHub Project #1 to repository<br>• Defined [ERROR_TAXONOMY.md](ERROR_TAXONOMY.md) |

---

## 🗓️ 12-Week Feature Roadmap & Assignments

### 🔹 Phase 1: Planning & Architecture (Weeks 1–3)
- [x] **Week 1:** Project initialization, requirements gathering, and Kanban board establishment. *(Lead: @sdPrang0n)*
- [x] **Week 2:** Printer error taxonomy specification ([ERROR_TAXONOMY.md](ERROR_TAXONOMY.md)).
- [ ] **Week 3:** System architecture design and component interface definitions.

### 🔹 Phase 2: Virtual Printer Core (Weeks 4–6)
- [ ] **Week 4:** Virtual printer connection listener and transport layer setup.
- [ ] **Week 5:** Stream buffering, chunk reception, and raw payload capture.
- [ ] **Week 6:** Virtual printer status reporting and heartbeat monitoring.

### 🔹 Phase 3: Error Detection Engine (Weeks 7–9)
- [ ] **Week 7:** Protocol and stream syntax validation (detecting malformed print instructions).
- [ ] **Week 8:** Network fault detection (incomplete transmission, timeout, socket abort).
- [ ] **Week 9:** Payload integrity and corruption detection (checksum mismatch, unexpected control bytes).

### 🔹 Phase 4: Diagnostics, Testing & Final Review (Weeks 10–12)
- [ ] **Week 10:** Error reporting module and diagnostic log generator.
- [ ] **Week 11:** Error injection test harness and validation runs.
- [ ] **Week 12:** Final project review, documentation wrap-up, and project handover.
