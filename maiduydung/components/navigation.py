"""Navigation component."""

import reflex as rx


def navbar() -> rx.Component:
    """Clean navigation bar with white background and blue accents."""
    return rx.box(
        rx.container(
            rx.hstack(
                # Logo
                rx.link(
                    rx.heading(
                        "Mai Duy Dung",
                        size="6",
                        weight="bold",
                        class_name="text-blue-600",
                    ),
                    href="/",
                ),
                # Navigation links
                rx.hstack(
                    rx.link(
                        "Home",
                        href="/",
                        class_name="text-gray-700 hover:text-blue-600 font-medium transition-colors",
                    ),
                    rx.link(
                        "Skills",
                        href="/skills",
                        class_name="text-gray-700 hover:text-blue-600 font-medium transition-colors",
                    ),
                    rx.link(
                        "Tech Stack",
                        href="/tech",
                        class_name="text-gray-700 hover:text-blue-600 font-medium transition-colors",
                    ),
                    rx.link(
                        "Contact",
                        href="/contact",
                        class_name="text-gray-700 hover:text-blue-600 font-medium transition-colors",
                    ),
                    spacing="6",
                    display=["none", "none", "flex"],
                ),
                # CTA Button
                rx.link(
                    rx.button(
                        "Let's Talk",
                        size="3",
                        variant="solid",
                        class_name="bg-blue-600 hover:bg-blue-700",
                    ),
                    href="/contact",
                ),
                justify="between",
                align="center",
                width="100%",
            ),
            max_width="1200px",
        ),
        class_name="bg-white border-b border-gray-200 py-4 px-4 sticky top-0 z-50",
    )

