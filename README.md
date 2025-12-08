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

### 2. The Orchestration Dashboard

---

## 🏗 Architecture

The system follows an **Event-Driven Microservices** pattern, fully containerized and orchestrated by Docker.
