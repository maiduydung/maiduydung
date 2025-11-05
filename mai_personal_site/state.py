import reflex as rx


class State(rx.State):
    """The app state."""

    name: str = "Mai"
    title: str = "Trilingual Data & ML Engineer"
    languages: str = "English / Vietnamese / Japanese"
    tagline: str = "I build end-to-end data and AI systems for fast-moving startups and SaaS companies."
    locations: str = "Tokyo, Shanghai, Vancouver, NYC, and SF"
    nav_links: list[dict[str, str]] = [
        {"name": "About", "href": "#about"},
        {"name": "Services", "href": "#services"},
        {"name": "My Works", "href": "#works"},
        {"name": "Tech Stack", "href": "#stack"},
        {"name": "Why Me", "href": "#why-me"},
        {"name": "Contact", "href": "#contact"},
    ]
    show_dialog_for_image: str = ""

    @rx.event
    def toggle_image_dialog(self, image_src: str):
        if self.show_dialog_for_image == image_src:
            self.show_dialog_for_image = ""
        else:
            self.show_dialog_for_image = image_src

    services: list[dict[str, str]] = [
        {
            "icon": "cloud",
            "title": "Cloud-Native Data Infra",
            "description": "I design and deploy scalable pipelines using the Azure ecosystem. Everything is clean, tested, and production-ready.",
        },
        {
            "icon": "search",
            "title": "Web Scraping at Scale",
            "description": "I use Playwright and automation to gather structured data that stays fresh and compliant.",
        },
        {
            "icon": "bar-chart-2",
            "title": "Real-Time and Batch Analytics",
            "description": "I build lightweight reporting stacks to help teams act fast on what the data says.",
        },
        {
            "icon": "cpu",
            "title": "Applied ML & AI",
            "description": "I deploy LLM-based systems, monitor models in prod, and accelerate them with ONNX or specialized hardware.",
        },
        {
            "icon": "briefcase",
            "title": "VC Tools & Real Estate Intelligence",
            "description": "I build full-stack platforms for investor workflows, deal sourcing, and property ROI analysis.",
        },
    ]
    tech_stack: list[dict[str, str | list[str]]] = [
        {
            "category": "Backend",
            "items": ["FastAPI", "Azure Functions", "Container Apps", "Service Bus"],
        },
        {
            "category": "Data & ML",
            "items": ["PSQL", "DuckDB", "PyTorch", "PyCaret", "ONNX", "MLflow"],
        },
        {
            "category": "Infra",
            "items": ["Azure (Cosmos DB, Blob, Service Bus)", "Docker", "Terraform"],
        },
        {
            "category": "Scraping & Automation",
            "items": ["Playwright", "Requests", "BeautifulSoup"],
        },
        {
            "category": "Dashboards & Analytics",
            "items": ["Streamlit", "Gradio", "Azure Dashboard", "Grafana"],
        },
        {
            "category": "Vector DB & AI",
            "items": ["FAISS", "PGVector", "LangChain", "LlamaIndex"],
        },
    ]
    why_me: list[dict[str, str]] = [
        {
            "icon": "briefcase",
            "title": "Founder Mindset, Builder Execution",
            "description": "I code like a builder and think like a founder. I understand the business context behind the technical requirements.",
        },
        {
            "icon": "users",
            "title": "Led Data Infra at a SaaS Startup",
            "description": "I have hands-on experience building and leading data infrastructure in a fast-paced, high-growth environment.",
        },
        {
            "icon": "globe-2",
            "title": "Async & Cross-Timezone Native",
            "description": "I'm experienced in working with distributed teams. No hand-holding required; I deliver results independently.",
        },
        {
            "icon": "shield-check",
            "title": "Fast, Reliable & Battle-Tested",
            "description": "My solutions are not academic exercises. They are battle-tested in production and built to be reliable and performant.",
        },
    ]
    project_highlights: list[dict[str, str]] = [
        {
            "icon": "trending-up",
            "title": "SaaS & Azure Expertise",
            "description": "A contract data/ML engineer with deep SaaS and Azure chops.",
        },
        {
            "icon": "download-cloud",
            "title": "Rapid Pipelines",
            "description": "Scraping and ingestion pipelines done fast and right.",
        },
        {
            "icon": "layout-dashboard",
            "title": "Turnkey Tools",
            "description": "A dashboard or AI tool that works out of the box.",
        },
    ]
    works: list[dict[str, str | list[str]]] = [
        {
            "title": "Secure, Secretless CI/CD for Azure",
            "summary": "Automated deployment for Azure Functions & Container Apps using GitHub Actions with OIDC and Managed Identities, eliminating the need for stored secrets.",
            "highlights": [
                "GitHub Actions & OIDC",
                "Azure Managed Identity",
                "Role-Based Access Control (RBAC)",
                "Terraform for IaC",
                "Federated Credentials",
                "Zero-Secret Deployment",
            ],
            "impact": "Established an enterprise-grade, compliant pipeline that scales across environments. Reduced security risks and automated deployments, allowing developers to ship faster.",
        },
        {
            "title": "Real-Time Real Estate Data Dashboard",
            "summary": "An operational observability layer for a real estate data platform, providing live insights into data freshness, coverage, and pipeline health.",
            "image": "/placeholder.svg",
            "highlights": [
                "Streamlit on Azure Container Apps",
                "Live Cosmos DB & Blob Storage Connection",
                "Real-Time Metrics Aggregation",
                "Automated Health Checks",
                "Data Coverage Visualizations",
                "ROI & Enhancement Tracking",
            ],
            "impact": "Provided a single source of truth for data operations, enabling the team to monitor ingestion health and ROI. Increased client trust through transparent reporting.",
        },
        {
            "title": "AI-Powered Property Classification",
            "summary": "An event-driven workflow that automatically classifies real estate properties (Turnkey, Light Maintenance, Fixer-Upper) using metadata and image analysis.",
            "image": "/placeholder.svg",
            "highlights": [
                "Azure Functions & Service Bus",
                "Concurrent Container App Workers",
                "Event-Driven Architecture",
                "Hybrid Inference (ML & rules)",
                "Scalable Image Processing",
                "Cosmos DB for state management",
            ],
            "impact": "Automated a high-value business process, enabling rapid property valuation and tagging. The system processes thousands of listings daily, enriching the core dataset.",
        },
    ]