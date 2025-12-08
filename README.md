# 🛡️ Sentinel: Autonomous AIOps & Self-Healing Agent

![Project Status](https://img.shields.io/badge/Status-v1.0-success?style=flat-square&color=4CAF50)
![Docker](https://img.shields.io/badge/Containerization-Docker-blue?style=flat-square&logo=docker)
![Python](https://img.shields.io/badge/Backend-FastAPI-009688?style=flat-square&logo=fastapi)
![AI](https://img.shields.io/badge/AI-Gemini%201.5%20Flash-orange?style=flat-square&logo=google)

**Sentinel** is an autonomous DevOps agent designed to monitor microservices, detect application crashes in real-time, and generate root-cause analysis and code fixes automatically.

Unlike standard chatbots, Sentinel implements an **LLM-Backed Semantic Cache**. It remembers previous errors and their solutions using a local SQL layer (Symbolic RAG), ensuring 100% precision for recurring incidents while reducing AI inference costs by over 90%.

---

## 📸 Demo & Screenshots

### 1. The Autonomous Fix Alert
<img width="1397" height="619" alt="image" src="https://github.com/user-attachments/assets/1998cde1-ffe3-4bfa-aef7-1476c7b212e1" />
<img width="636" height="781" alt="image" src="https://github.com/user-attachments/assets/23e21ec3-93cb-4777-aa55-8d6c6d7795cc" />

### 2. The Orchestration Dashboard
<img width="663" height="407" alt="image" src="https://github.com/user-attachments/assets/a8850ced-df29-4c80-a1d2-d73a14543f13" />

---

## 🏗 Architecture

The system follows an **Event-Driven Microservices** pattern, fully containerized and orchestrated by Docker.
<img width="1070" height="340" alt="image" src="https://github.com/user-attachments/assets/7c71362f-cb4e-4855-9f9d-413a5e4aacb8" />

## 🔮 Roadmap & Future Improvements

While v1.0 demonstrates the core autonomous cycle, the following features are planned for v2.0 to move towards a fully Agentic workflow:

- [ ] **GitHub Integration (Auto-PRs):** Instead of sending code snippets via email, the agent will use the GitHub API to open a Pull Request with the fix, allowing for one-click merges.
- [ ] **Source Code Context:** The Brain will be upgraded to read the actual source file (e.g., `main.py`) around the line of the crash to provide logic-aware fixes rather than just stack-trace analysis.
- [ ] **Reinforcement Learning Loop:** Implementation of interactive Slack buttons ("Approvel/Reject"). Rejected fixes will be flagged in the database to prevent the AI from suggesting failed solutions again.
- [ ] **Vector Database Migration:** For larger codebases, migrating from SQLite to **pgvector** (PostgreSQL) to support semantic search across documentation and internal wikis.
