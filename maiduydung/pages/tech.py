"""Tech Stack page."""

import reflex as rx
from ..components import navbar, footer


def techBadge(text: str) -> rx.Component:
    """Clean tech badge component."""
    return rx.box(
        rx.text(
            text,
            size="3",
            weight="medium",
            class_name="text-blue-700",
        ),
        class_name="px-4 py-2 bg-blue-50 hover:bg-blue-100 rounded-full border border-blue-200 transition-all cursor-default",
    )


def techSection(title: str, *technologies) -> rx.Component:
    """Tech category section."""
    return rx.vstack(
        rx.heading(
            title,
            size="5",
            weight="bold",
            class_name="text-gray-900",
        ),
        rx.box(
            *[techBadge(tech) for tech in technologies],
            display="flex",
            flex_wrap="wrap",
            gap="3",
        ),
        spacing="5",
        align="start",
        width="100%",
    )


def tech_page() -> rx.Component:
    """Tech stack page."""
    return rx.box(
        navbar(),
        # Main content container
        rx.box(
            rx.flex(
                rx.vstack(
                    # Page Header
                    rx.vstack(
                        rx.heading(
                            "Tech Stack",
                            size="9",
                            weight="bold",
                            class_name="text-gray-900",
                        ),
                        rx.text(
                            "Modern tools and frameworks I use to deliver results",
                            size="5",
                            class_name="text-gray-600",
                        ),
                        spacing="3",
                        align="center",
                    ),
                    # Tech Grid
                    rx.vstack(
                        techSection(
                            "Backend & APIs",
                            "FastAPI",
                            "Azure Functions",
                            "Container Apps",
                            "Service Bus",
                        ),
                        techSection(
                            "Data & ML",
                            "PostgreSQL",
                            "DuckDB",
                            "PyTorch",
                            "PyCaret",
                            "ONNX",
                            "MLflow",
                        ),
                        techSection(
                            "Cloud Infrastructure",
                            "Azure Cosmos DB",
                            "Azure Blob Storage",
                            "Docker",
                            "Terraform",
                        ),
                        techSection(
                            "Web Scraping & Automation",
                            "Playwright",
                            "Requests",
                            "BeautifulSoup",
                        ),
                        techSection(
                            "Analytics & Dashboards",
                            "Streamlit",
                            "Gradio",
                            "Azure Dashboard",
                            "Grafana",
                        ),
                        techSection(
                            "Vector DB & AI",
                            "FAISS",
                            "PGVector",
                            "LangChain",
                            "LlamaIndex",
                        ),
                        spacing="9",
                        width="100%",
                        class_name="bg-white p-10 rounded-lg border border-gray-200 shadow-sm",
                    ),
                    # Bottom CTA
                    rx.vstack(
                        rx.heading(
                            "Ready to Build?",
                            size="6",
                            weight="bold",
                            class_name="text-gray-900",
                        ),
                        rx.text(
                            "Let's discuss your project and see how I can help.",
                            class_name="text-gray-600",
                        ),
                        rx.link(
                            rx.button(
                                "Get In Touch",
                                size="4",
                                variant="solid",
                                class_name="bg-blue-600 hover:bg-blue-700",
                            ),
                            href="/contact",
                        ),
                        spacing="4",
                        align="center",
                        class_name="bg-blue-50 p-10 rounded-lg border border-blue-200",
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

