"""Contact page."""

import reflex as rx
from ..components import navbar, footer


def contact_page() -> rx.Component:
    """Contact page with CTA."""
    return rx.box(
        navbar(),
        # Main content container
        rx.box(
            rx.flex(
                rx.vstack(
                    # Page Header
                    rx.vstack(
                        rx.heading(
                            "Let's Work Together",
                            size="9",
                            weight="bold",
                            class_name="text-gray-900",
                        ),
                        rx.text(
                            "Open for short-term projects and contract work",
                            size="5",
                            class_name="text-gray-600",
                        ),
                        spacing="3",
                        align="center",
                    ),
                    # Pitch
                    rx.text(
                        "You don't need a full-time hire. You need someone who can hit the ground running, clean up the mess, ship results, and move on. That's what I do.",
                        size="5",
                        class_name="text-gray-700 text-center max-w-3xl",
                        line_height="1.7",
                    ),
                    # What I offer
                    rx.vstack(
                        rx.heading(
                            "I'm a great fit if you need:",
                            size="5",
                            weight="bold",
                            class_name="text-gray-900",
                        ),
                        rx.vstack(
                            rx.hstack(
                                rx.text("✓", class_name="text-blue-600 font-bold"),
                                rx.text(
                                    "A contract data/ML engineer with SaaS and Azure expertise",
                                    class_name="text-gray-700",
                                ),
                                align="start",
                                spacing="3",
                            ),
                            rx.hstack(
                                rx.text("✓", class_name="text-blue-600 font-bold"),
                                rx.text(
                                    "Scraping and data ingestion pipelines done fast and right",
                                    class_name="text-gray-700",
                                ),
                                align="start",
                                spacing="3",
                            ),
                            rx.hstack(
                                rx.text("✓", class_name="text-blue-600 font-bold"),
                                rx.text(
                                    "A dashboard or AI tool that works out of the box",
                                    class_name="text-gray-700",
                                ),
                                align="start",
                                spacing="3",
                            ),
                            rx.hstack(
                                rx.text("✓", class_name="text-blue-600 font-bold"),
                                rx.text(
                                    "Someone who codes like a builder and thinks like a founder",
                                    class_name="text-gray-700",
                                ),
                                align="start",
                                spacing="3",
                            ),
                            spacing="3",
                            align="start",
                        ),
                        spacing="5",
                        align="start",
                        class_name="bg-gray-50 p-8 rounded-lg border border-gray-200 max-w-2xl w-full",
                    ),
                    # Contact Buttons
                    rx.vstack(
                        rx.heading(
                            "Get In Touch",
                            size="5",
                            weight="bold",
                            class_name="text-gray-900",
                        ),
                        rx.hstack(
                            rx.link(
                                rx.button(
                                    rx.hstack(
                                        rx.text("📩"),
                                        rx.text("maiduydungvn@gmail.com"),
                                        spacing="2",
                                    ),
                                    size="4",
                                    variant="solid",
                                    class_name="bg-blue-600 hover:bg-blue-700",
                                ),
                                href="mailto:maiduydungvn@gmail.com",
                                is_external=True,
                            ),
                            rx.link(
                                rx.button(
                                    rx.hstack(
                                        rx.text("💼"),
                                        rx.text("LinkedIn"),
                                        spacing="2",
                                    ),
                                    size="4",
                                    variant="outline",
                                    class_name="border-blue-600 text-blue-600 hover:bg-blue-50",
                                ),
                                href="https://www.linkedin.com/in/maiduydung/",
                                is_external=True,
                            ),
                            rx.link(
                                rx.button(
                                    rx.hstack(
                                        rx.text("📅"),
                                        rx.text("Book a Call"),
                                        spacing="2",
                                    ),
                                    size="4",
                                    variant="outline",
                                    class_name="border-blue-600 text-blue-600 hover:bg-blue-50",
                                ),
                                href="https://calendly.com/maiduydungvn/meeting-with-mai",
                                is_external=True,
                            ),
                            spacing="4",
                            wrap="wrap",
                            justify="center",
                        ),
                        spacing="4",
                        align="center",
                    ),
                    # Why work with me
                    rx.vstack(
                        rx.heading(
                            "Why Work With Me",
                            size="5",
                            weight="bold",
                            class_name="text-gray-900",
                        ),
                        rx.vstack(
                            rx.text("⚡ Fast, reliable, battle-tested in production", class_name="text-gray-700"),
                            rx.text("🌐 Cross-timezone, async-native, no hand-holding needed", class_name="text-gray-700"),
                            rx.text("🏢 Built and led data infra at a fast-growing SaaS startup", class_name="text-gray-700"),
                            rx.text("🎯 Only real solutions, no fluff or AI theater", class_name="text-gray-700"),
                            spacing="3",
                            class_name="bg-blue-50 p-6 rounded-lg border border-blue-200 max-w-2xl w-full",
                        ),
                        spacing="4",
                        align="center",
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
        class_name="bg-white min-h-screen",
    )

