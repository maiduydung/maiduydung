## Hi, I'm Mai Duy Dung

**CEO & Founder of Pathfinder Softworks** — AI agents, data systems, and automation for companies that make and move physical things.

Based in Saigon, Vietnam. Lived in Japan for 7 years (MEXT scholarship + engineering work). I speak English, Vietnamese, and Japanese.

I don't build "AI demos." I build systems that replace chaos. Pipelines that don't break. Automation that saves money. Decision tools backed by real data. Deterministic logic where it's reliable, LLM reasoning where it adds real value.

---

### Pathfinder Softworks

Software studio for SMEs in manufacturing and logistics — the businesses that run the physical economy but get ignored by enterprise software. We build the systems they actually need: operations tooling, data pipelines, and AI agents that survive contact with real-world mess.

**Client work — trucking & truck manufacturing:**

- [`TruckerMobile`](https://github.com/maiduydung/TruckerMobile) + [`TruckerMobileBackend`](https://github.com/maiduydung/TruckerMobileBackend) Cross-platform trip logger for truck drivers. Expo (React Native) + Azure Functions + PostgreSQL. Built for drivers with minimal tech literacy. Every action is max 2 taps.

- [`nhutin-backend`](https://github.com/maiduydung/nhutin-backend) Real-time BOM optimization for a truck body manufacturer. 4-phase constrained feasibility algorithm that solves material requirements planning under real inventory constraints.

**Multi-agent systems for real domains:**

- [`financial_agents`](https://github.com/maiduydung/financial_agents) Company analyst agent: RAG over financial docs, live market data, web research. LangGraph orchestration, Streamlit UI with real-time agent activity logs.

- [`medical-agents`](https://github.com/maiduydung/medical-agents) Real-time vitals monitoring with multi-agent triage. Deterministic rules handle the common path ($0 LLM cost), specialist agents activate only on anomalies. Azure Service Bus + LangGraph + Chroma + openFDA APIs.

- [`FlowShot`](https://github.com/maiduydung/FlowShot) CLI/library that reads codebases and generates branded workflow diagrams via LLM. Point it at repos, get SVGs. `pip install flowshot`.

---

### Recent: Outrider — on-prem LLM for smart buildings

LLM-powered operations assistant for commercial facilities (hospitality, building automation, energy management) — running **entirely on-site on a single edge box**. No cloud, no data egress, no per-token bill. The building's data never leaves the building.

- **Edge inference under real constraints:** quantized open-weight models (FP4) served with vLLM on NVIDIA Jetson-class hardware. Model selection driven by hands-on benchmarking across model families under tight memory and thermal budgets — the best model on a leaderboard is rarely the best model on a 60W box.
- **Deterministic agent workflows:** the LLM proposes, deterministic policy disposes. Hard safety floors on anything that touches physical controls — in building systems, "the model hallucinated" is not an acceptable failure mode.
- **Appliance-grade packaging:** model + runtime + agent workflows shipped as a self-contained unit that can be racked on-site and run offline.

---

### Past work

**AI/Data Pipeline for [Proplytics](https://www.proplytics.net/): U.S. SaaS Real Estate Investment Analytics**

Proplytics helped property investors instantly evaluate any U.S. property: ROI, cap rate, cash flow projections, and dual rental strategy comparison (long-term vs. short-term/Airbnb). I built the data infrastructure that made it possible — a distributed pipeline continuously ingesting, validating, and enriching property data across multiple U.S. states:

- **National-scale scraping pipeline**: crawls and ingests property listings across the U.S. on Azure Functions, multi-source with deduplication, retry logic, and intelligent caching
- **Medallion architecture on Azure**: raw ingest (bronze) -> cleaned and validated (silver) -> analytics-ready (gold). Cosmos DB for operational data, snapshotted to Parquet files and loaded into DuckDB for fast columnar analytics served directly from Next.js. Redis for low-latency reads.
- **ML rental prediction with MLOps**: models trained on scraped data, automated retraining pipelines, model versioning and monitoring in production
- **Sub-second similarity search**: DuckDB columnar engine + pre-computed ZIP spatial relationships, ranked comparables across hundreds of thousands of records in milliseconds
- **AI enrichment microservices**: LLM-assisted multifamily unit estimation, multi-source reconciliation with automatic fallback

**Stack**: Next.js · Python · Azure Functions · Azure Cosmos DB · DuckDB · Azure Cognitive Search · Azure Service Bus

[github.com/proplytics](https://github.com/proplytics/)

---

### Stack

- **AI/Agents:** LangGraph, LangChain, Chroma, FAISS, PGVector · local-LLM / edge deployment (vLLM, quantized models on edge hardware)
- **Backend:** Python, FastAPI, Azure Functions, Azure Container Apps, Service Bus
- **Frontend:** TypeScript, React Native (Expo), SvelteKit
- **Infra:** Azure, Docker, GitHub Actions

---

### How I work

I build with Claude Code daily. Not as autocomplete, but as a collaborator in agentic workflows. Most of what's in these repos was built AI-natively: architecture by me, implementation in tight loops with LLMs, every line reviewed and understood.

Every repo has a `CLAUDE.md` and governance rules. I treat LLM-readability as a first-class requirement. If an AI can't understand your codebase, a new hire won't either.

---

### Let's talk

If you run a manufacturing or logistics business drowning in spreadsheets and manual ops — that's exactly the problem Pathfinder exists for. Also open to partnerships, consulting engagements, and interesting problems.

[maiduydungvn@gmail.com](mailto:maiduydungvn@gmail.com) / [LinkedIn](https://www.linkedin.com/in/maiduydung/)
