## Hi, I'm Mai Duy Dung (Mike)

Founder @ **Pathfinder Softworks** -- building data systems and AI agents for companies that make physical things.

Based in Vietnam. Lived in Japan for 7 years (MEXT scholarship + engineering work). I speak English, Vietnamese, and Japanese.

### What I'm building

**Multi-agent systems for real domains:**

- [`medical-agents`](https://github.com/maiduydung/medical-agents) -- Real-time vitals monitoring with multi-agent triage. Deterministic rules handle the common path ($0 LLM cost); specialist agents (cardiac, respiratory, general) activate only on anomalies. Azure Service Bus + LangGraph + Chroma + openFDA APIs.

- [`financial_agents`](https://github.com/maiduydung/financial_agents) -- Company analyst agent: RAG over financial docs, live market data, web research. LangGraph orchestration, Streamlit UI with real-time agent activity logs.

- [`FlowShot`](https://github.com/maiduydung/FlowShot) -- CLI/library that reads codebases and generates branded workflow diagrams via LLM. Point it at repos, get SVGs. `pip install flowshot`.

**Production software for a trucking SME (NhuTin):**

- [`TruckerMobile`](https://github.com/maiduydung/TruckerMobile) + [`TruckerMobileBackend`](https://github.com/maiduydung/TruckerMobileBackend) -- Cross-platform trip logger for truck drivers. Expo (React Native) + Azure Functions + PostgreSQL. Designed for drivers with minimal tech literacy -- every action is max 2 taps.

- **nhutin-backend** (private) -- Real-time BOM optimization for manufacturing. Solves material requirements planning for a mid-size operation.

### Stack

**AI/Agents:** LangGraph, LangChain, Chroma, FAISS, PGVector
**Backend:** Python, FastAPI, Azure Functions, Azure Container Apps, Service Bus
**Frontend:** TypeScript, React Native (Expo), SvelteKit
**Infra:** Azure, Docker, GitHub Actions

### How I work

I build with Claude Code daily -- not as autocomplete, but as a collaborator in agentic workflows. Most of what's in these repos was built AI-natively: architecture by me, implementation in tight loops with LLMs, every line reviewed and understood.

I care about systems that combine domain knowledge with AI -- deterministic logic where it's reliable, LLM reasoning where it adds real value. No AI theater.

### Contact

[maiduydungvn@gmail.com](mailto:maiduydungvn@gmail.com) / [LinkedIn](https://www.linkedin.com/in/maiduydung/)
