## Hi, I'm Mai Duy Dung

Data & ML Engineer. I build data systems, automation, and AI agents for companies that make physical things.

Based in Saigon, Vietnam. Lived in Japan for 7 years (MEXT scholarship + engineering work). I speak English, Vietnamese, and Japanese.

I don't build "AI demos." I build systems that replace chaos. Pipelines that don't break. Automation that saves money. Decision tools backed by real data. Deterministic logic where it's reliable, LLM reasoning where it adds real value.

---

### What I'm building

**AI/Data Pipeline for [Proplytics](https://www.proplytics.net/): U.S. SaaS Real Estate Investment Analytics**

[Proplytics](https://www.proplytics.net/) helps property investors instantly evaluate any U.S. property: ROI, cap rate, cash flow projections, and dual rental strategy comparison (long-term vs. short-term/Airbnb). Work that used to take hours of spreadsheet grinding, delivered in seconds.

I built the data infrastructure that makes this possible: a distributed pipeline that continuously ingests, validates, and enriches property data across multiple U.S. states. Key engineering pieces:

- **National-scale scraping pipeline**: crawls and ingests property listings across the U.S. on Azure Functions, multi-source with deduplication, retry logic, and intelligent caching
- **Medallion architecture on Azure**: raw ingest (bronze) -> cleaned and validated (silver) -> analytics-ready (gold). Cosmos DB for operational data, snapshotted to Parquet files and loaded into DuckDB for fast columnar analytics served directly from Next.js. Redis for low-latency reads.
- **ML rental prediction with MLOps**: models trained on scraped data, automated retraining pipelines, model versioning and monitoring in production
- **Sub-second similarity search**: DuckDB columnar engine + pre-computed ZIP spatial relationships, ranked comparables across hundreds of thousands of records in milliseconds
- **AI enrichment microservices**: LLM-assisted multifamily unit estimation, multi-source reconciliation with automatic fallback

**Stack**: Next.js · Python · Azure Functions · Azure Cosmos DB · DuckDB · Azure Cognitive Search · Azure Service Bus

[github.com/proplytics](https://github.com/proplytics/)

**Past work for a trucking SME:**

- [`TruckerMobile`](https://github.com/maiduydung/TruckerMobile) + [`TruckerMobileBackend`](https://github.com/maiduydung/TruckerMobileBackend) Cross-platform trip logger for truck drivers. Expo (React Native) + Azure Functions + PostgreSQL. Built for drivers with minimal tech literacy. Every action is max 2 taps.

- [`nhutin-backend`](https://github.com/maiduydung/nhutin-backend) Real-time BOM optimization for a truck body manufacturer. 4-phase constrained feasibility algorithm that solves material requirements planning under real inventory constraints.

**Multi-agent systems for real domains:**

- [`financial_agents`](https://github.com/maiduydung/financial_agents) Company analyst agent: RAG over financial docs, live market data, web research. LangGraph orchestration, Streamlit UI with real-time agent activity logs.

- [`medical-agents`](https://github.com/maiduydung/medical-agents) Real-time vitals monitoring with multi-agent triage. Deterministic rules handle the common path ($0 LLM cost), specialist agents activate only on anomalies. Azure Service Bus + LangGraph + Chroma + openFDA APIs.

- [`FlowShot`](https://github.com/maiduydung/FlowShot) CLI/library that reads codebases and generates branded workflow diagrams via LLM. Point it at repos, get SVGs. `pip install flowshot`.

---

### Stack

- **AI/Agents:** LangGraph, LangChain, Chroma, FAISS, PGVector
- **Backend:** Python, FastAPI, Azure Functions, Azure Container Apps, Service Bus
- **Frontend:** TypeScript, React Native (Expo), SvelteKit
- **Infra:** Azure, Docker, GitHub Actions

---

### How I work

I build with Claude Code daily. Not as autocomplete, but as a collaborator in agentic workflows. Most of what's in these repos was built AI-natively: architecture by me, implementation in tight loops with LLMs, every line reviewed and understood.

Every repo has a `CLAUDE.md` and governance rules. I treat LLM-readability as a first-class requirement. If an AI can't understand your codebase, a new hire won't either.

---

### Let's talk

Open to partnerships, consulting engagements, and interesting problems.

[maiduydungvn@gmail.com](mailto:maiduydungvn@gmail.com) / [LinkedIn](https://www.linkedin.com/in/maiduydung/)
