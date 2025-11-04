"""Footer component."""

import reflex as rx


def footer() -> rx.Component:
    """Simple footer with copyright."""
    return rx.box(
        rx.container(
            rx.vstack(
                rx.divider(class_name="mb-6"),
                rx.hstack(
                    rx.text(
                        "© 2025 Mai Duy Dung",
                        class_name="text-gray-600",
                    ),
                    rx.hstack(
                        rx.link(
                            "LinkedIn",
                            href="https://www.linkedin.com/in/maiduydung/",
                            is_external=True,
                            class_name="text-blue-600 hover:text-blue-700",
                        ),
                        rx.text("•", class_name="text-gray-400"),
                        rx.link(
                            "Email",
                            href="mailto:maiduydungvn@gmail.com",
                            is_external=True,
                            class_name="text-blue-600 hover:text-blue-700",
                        ),
                        spacing="3",
                    ),
                    justify="between",
                    width="100%",
                    class_name="flex-col sm:flex-row",
                ),
                spacing="4",
                padding_y="8",
            ),
            max_width="1200px",
        ),
        class_name="bg-white",
    )

