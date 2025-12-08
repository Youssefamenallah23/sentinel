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
