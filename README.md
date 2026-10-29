# FastAPI Clean Architecture & DDD Template 🏛️

[![NexusPulse EdgeSaaS](https://raw.githubusercontent.com/MilindChatrabhuji/nexus-edgesaas/main/distribution/digital_assets/edgesaas-banner-readme.svg)](https://edgesaas.nexus-pulse.com)

> ⚡ **Building edge-first Micro-SaaS?** Check out [**NexusPulse EdgeSaaS**](https://edgesaas.nexus-pulse.com) — production Cloudflare Workers boilerplate with /mo idle cost, Hono, Stripe billing, and Web Crypto auth.

---


[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![FastAPI](https://img.shields.io/badge/Framework-FastAPI-009688.svg)](https://fastapi.tiangolo.com/)
[![Pydantic v2](https://img.shields.io/badge/Pydantic-v2.0+-e92063.svg)](https://docs.pydantic.dev/)
[![Clean Architecture](https://img.shields.io/badge/Design-DDD%20%26%20Clean%20Arch-blue.svg)](https://blog.cleancoder.com/)

A production-grade, highly maintainable **FastAPI starter kit** implementing **Clean Architecture** and **Domain-Driven Design (DDD)** principles with **Pydantic v2**, async repositories, and dependency injection.

---

## 🏗️ Architectural Topology

```
app/
├── domain/            # Enterprise Business Rules (Entities, Value Objects, Domain Exceptions)
├── application/       # Application Business Rules (Use Cases, DTOs, Service Interfaces)
├── infrastructure/    # Frameworks & Drivers (SQLAlchemy, Redis, External APIs, Adapters)
└── presentation/      # Interface Adapters (FastAPI Routers, Dependency Injection, Schemas)
```

---

## 🚀 Getting Started

### 1. Installation

```bash
git clone https://github.com/MilindChatrabhuji/fastapi-clean-architecture.git
cd fastapi-clean-architecture
pip install fastapi uvicorn pydantic
```

### 2. Run the API Server

```bash
uvicorn app.main:app --reload --port 8000
```
Open interactive Swagger docs at `http://localhost:8000/docs`.

---

## 🧪 Testing

```bash
python -m pytest tests
```

---

## 📄 License
MIT License. Architected by [Milind Chatrabhuji](https://github.com/MilindChatrabhuji).
