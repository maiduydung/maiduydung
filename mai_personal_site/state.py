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
            "items": ["FastAPI", "Function Apps", "Container Apps", "Service Bus", "Logic Apps"],
        },
        {
            "category": "Data & ML",
            "items": ["PSQL", "DuckDB", "PyTorch", "PyCaret", "ONNX", "MLflow"],
        },
        {
            "category": "Infra",
            "items": ["Azure", "Docker", "GitHub Actions", "Terraform"],
        },
        {
            "category": "Scraping & Automation",
            "items": ["Playwright", "Botasaurus", "Requests", "BeautifulSoup"],
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
            "title": "AI-Powered Property Classification",
            "summary": "We automatically find and categorize properties (Turnkey, Light Work, Fixer) from online listings. Photos and details are processed within minutes so your team sees consistent, ready-to-use labels across thousands of homes.",
            "image": "/project_pics/zillow_image_scraper.jpg",
            "highlights": [
                "Technical highlights: web scraper, event queue, async workers",
                "Azure Functions, Logic Apps, Service Bus",
                "Blob Storage & Cosmos DB for data and state",
                "Image classification (ML + rules) with caching",
            ],
            "impact": "Less manual review, faster underwriting, and a richer dataset. The system handles thousands of listings daily and keeps quality high while costs stay low.",
        },
        {
            "title": "Real-Time Real Estate Data Dashboard",
            "summary": "A single place to see what data you have, how fresh it is, where gaps exist, and whether everything is running smoothly. Built for quick daily check-ins and investor-ready reporting.",
            "image": "/project_pics/proplytics_dashboard.jpg",
            "highlights": [
                "Technical highlights: Streamlit on Azure Container Apps",
                "Live data from Cosmos DB & Blob Storage",
                "Automated health checks and metrics",
                "Coverage and freshness visualizations",
            ],
            "impact": "Gives leaders a reliable picture in seconds-fewer blind spots, quicker decisions, and clearer conversations with stakeholders and clients.",
        },
        {
            "title": "Secure, Secretless CI/CD for Azure",
            "summary": "Code changes go live safely with one click, no shared passwords or keys to manage. Releases are faster, safer, and easier to audit across environments.",
            "highlights": [
                "Technical highlights: GitHub Actions with OIDC",
                "Azure Managed Identity & RBAC",
                "Terraform-based infrastructure",
                "Zero stored secrets in pipelines",
            ],
            "impact": "Lower security risk, faster releases, and clean compliance trails-engineering moves quicker without compromising safety.",
        },
    ]