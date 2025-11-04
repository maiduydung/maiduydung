"""Home page - Hero section and introduction."""

import reflex as rx
from ..components import navbar, footer


def home_page() -> rx.Component:
    """Clean home page with hero section."""
    return rx.box(
        navbar(),
        # Hero Section
        rx.box(
            rx.flex(
                rx.vstack(
                    # Avatar
                    rx.image(
                        src="/avatar/mai_avatar.jpg",
                        width="150px",
                        height="150px",
                        border_radius="50%",
                        class_name="object-cover border-4 border-blue-600",
                    ),
                    # Main heading
                    rx.heading(
                        "Hi, I'm Mai 👋",
                        size="9",
                        weight="bold",
                        class_name="text-gray-900",
                    ),
                    # Subtitle
                    rx.text(
                        "Trilingual Data/ML Engineer",
                        size="6",
                        weight="medium",
                        class_name="text-blue-600",
                    ),
                    # Description
                    rx.text(
                        "I build end-to-end data and AI systems for fast-moving startups and SaaS companies.",
                        size="5",
                        class_name="text-gray-700 text-center max-w-2xl",
                        line_height="1.6",
                    ),
                    rx.text(
                        "With experience across Tokyo, Shanghai, Vancouver, NYC, and SF, I specialize in turning messy data into actionable insights that drive business results.",
                        size="4",
                        class_name="text-gray-600 text-center max-w-2xl",
                        line_height="1.7",
                    ),
                    # Languages
                    rx.hstack(
                        rx.badge("🇺🇸 English", size="2", variant="soft", color_scheme="blue"),
                        rx.badge("🇻🇳 Vietnamese", size="2", variant="soft", color_scheme="blue"),
                        rx.badge("🇯🇵 Japanese", size="2", variant="soft", color_scheme="blue"),
                        spacing="3",
                    ),
                    # CTA Buttons
                    rx.hstack(
                        rx.link(
                            rx.button(
                                "View My Skills",
                                size="4",
                                variant="solid",
                                class_name="bg-blue-600 hover:bg-blue-700",
                            ),
                            href="/skills",
                        ),
                        rx.link(
                            rx.button(
                                "Get In Touch",
                                size="4",
                                variant="outline",
                                class_name="border-blue-600 text-blue-600 hover:bg-blue-50",
                            ),
                            href="/contact",
                        ),
                        spacing="4",
                    ),
                    spacing="6",
                    align="center",
                    padding_y="12",
                    max_width="1200px",
                    width="100%",
                ),
                justify="center",
                align="center",
                width="100%",
            ),
            class_name="bg-white min-h-[80vh]",
        ),
        # Quick Highlights Section
        rx.box(
            rx.flex(
                rx.vstack(
                    rx.heading(
                        "Quick Highlights",
                        size="7",
                        weight="bold",
                        class_name="text-gray-900",
                    ),
                    rx.box(
                        # Card 1
                        rx.box(
                            rx.vstack(
                                rx.text("⚡", size="8"),
                                rx.heading("Fast Delivery", size="4", weight="bold", class_name="text-gray-900"),
                                rx.text(
                                    "Hit the ground running. No ramp-up, just results.",
                                    class_name="text-gray-600 text-center",
                                ),
                                spacing="3",
                                align="center",
                            ),
                            class_name="bg-white p-8 rounded-lg border border-gray-200 hover:border-blue-300 hover:shadow-lg transition-all",
                        ),
                        # Card 2
                        rx.box(
                            rx.vstack(
                                rx.text("🎯", size="8"),
                                rx.heading("Production-Ready", size="4", weight="bold", class_name="text-gray-900"),
                                rx.text(
                                    "Battle-tested code that scales and performs.",
                                    class_name="text-gray-600 text-center",
                                ),
                                spacing="3",
                                align="center",
                            ),
                            class_name="bg-white p-8 rounded-lg border border-gray-200 hover:border-blue-300 hover:shadow-lg transition-all",
                        ),
                        # Card 3
                        rx.box(
                            rx.vstack(
                                rx.text("🌐", size="8"),
                                rx.heading("Global Experience", size="4", weight="bold", class_name="text-gray-900"),
                                rx.text(
                                    "Cross-timezone, async-native work style.",
                                    class_name="text-gray-600 text-center",
                                ),
                                spacing="3",
                                align="center",
                            ),
                            class_name="bg-white p-8 rounded-lg border border-gray-200 hover:border-blue-300 hover:shadow-lg transition-all",
                        ),
                        display="grid",
                        grid_template_columns=["1fr", "1fr", "repeat(3, 1fr)"],
                        gap="6",
                    ),
                    spacing="8",
                    padding_y="16",
                    max_width="1200px",
                    width="100%",
                ),
                justify="center",
                width="100%",
            ),
            class_name="bg-gray-50",
        ),
        footer(),
        width="100%",
        class_name="bg-white",
    )

