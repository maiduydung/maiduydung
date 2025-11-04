"""Skills page - What I Do Best."""

import reflex as rx
from ..components import navbar, footer


def skillCard(emoji: str, title: str, description: str) -> rx.Component:
    """Clean skill card component."""
    return rx.box(
        rx.vstack(
            rx.text(emoji, size="9"),
            rx.heading(
                title,
                size="5",
                weight="bold",
                class_name="text-gray-900",
            ),
            rx.text(
                description,
                size="3",
                class_name="text-gray-600",
                line_height="1.7",
            ),
            spacing="4",
            align="start",
        ),
        class_name="bg-white p-8 rounded-lg border border-gray-200 hover:border-blue-400 hover:shadow-lg transition-all",
    )


def skills_page() -> rx.Component:
    """Skills page with service offerings."""
    return rx.box(
        navbar(),
        # Main content container
        rx.box(
            rx.flex(
                rx.vstack(
                    # Page Header
                    rx.vstack(
                        rx.heading(
                            "What I Do Best",
                            size="9",
                            weight="bold",
                            class_name="text-gray-900",
                        ),
                        rx.text(
                            "End-to-end data and AI solutions for modern companies",
                            size="5",
                            class_name="text-gray-600",
                        ),
                        spacing="3",
                        align="center",
                    ),
                    # Skills Grid
                    rx.box(
                        skillCard(
                            "☁️",
                            "Cloud-Native Data Infrastructure",
                            "I design and deploy scalable pipelines using the Azure ecosystem: Cosmos DB, Service Bus, Functions, Container Apps, and Blob Storage. Everything is clean, documented, and production-ready.",
                        ),
                        skillCard(
                            "🕷️",
                            "Web Scraping at Scale",
                            "Need Zillow-level data pulled daily? I use Playwright, rotating headers, proxies, and smart automation to gather structured data that stays fresh and compliant.",
                        ),
                        skillCard(
                            "📊",
                            "Real-Time & Batch Analytics",
                            "From PostgreSQL and DuckDB to Streamlit and Grafana—I build lightweight reporting stacks and internal tools to help teams act fast on what the data says.",
                        ),
                        skillCard(
                            "🤖",
                            "Applied ML & AI",
                            "I deploy LLM-based systems (agentic chatbots, RAG, MCP servers), monitor NLP and regression/classification models in prod, and accelerate them with ONNX when needed. Only real use cases, no AI theater.",
                        ),
                        skillCard(
                            "🏢",
                            "VC Tools & Real Estate Intelligence",
                            "Built full-stack platforms for investor workflows: deal sourcing, property ROI analysis, and vector database search, all tailored for decision-makers who need speed and accuracy.",
                        ),
                        skillCard(
                            "🚀",
                            "Contract & Startup-Ready",
                            "I work like a founder. Fast iterations, async communication, and zero hand-holding required. Perfect for short-term projects and SaaS companies that need to move fast.",
                        ),
                        display="grid",
                        grid_template_columns=["1fr", "1fr", "repeat(2, 1fr)"],
                        gap="6",
                    ),
                    spacing="9",
                    align="center",
                    max_width="1200px",
                    width="100%",
                    padding_x="4",
                    padding_y="12",
                ),
                justify="center",
                align="center",
                width="100%",
            ),
        ),
        footer(),
        width="100%",
        class_name="bg-gray-50 min-h-screen",
    )

