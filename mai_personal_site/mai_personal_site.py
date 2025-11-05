import reflex as rx
from mai_personal_site.state import State


def hero_section() -> rx.Component:
    """The hero section of the portfolio."""
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.span(
                        State.languages,
                        class_name="text-sm font-medium text-blue-600 bg-blue-100 px-3 py-1 rounded-full w-fit",
                    ),
                    rx.el.h1(
                        "Hi, I'm ",
                        rx.el.span(State.name, class_name="text-blue-600"),
                        f", a {State.title}",
                        class_name="text-4xl md:text-6xl font-bold text-gray-800 mt-4 leading-tight tracking-tighter",
                    ),
                    rx.el.p(
                        State.tagline, class_name="mt-6 text-lg text-gray-600 max-w-2xl"
                    ),
                    rx.el.p(
                        f"Proven track record across {State.locations}.",
                        class_name="mt-2 text-md text-gray-500",
                    ),
                    rx.el.div(
                        rx.el.a(
                            "Get In Touch",
                            href="#contact",
                            class_name="bg-blue-600 text-white font-semibold px-6 py-3 rounded-lg hover:bg-blue-700 transition-colors shadow-sm",
                        ),
                        rx.el.a(
                            "View My Work",
                            href="#works",
                            class_name="bg-white text-gray-700 font-semibold px-6 py-3 rounded-lg hover:bg-gray-100 transition-colors border border-gray-200",
                        ),
                        class_name="mt-8 flex gap-4",
                    ),
                    class_name="flex flex-col items-start md:w-2/3",
                ),
                rx.el.div(
                    rx.el.image(
                        src="/avatar/mai_avatar.jpg",
                        class_name="rounded-full object-cover w-64 h-64 md:w-80 md:h-80 border-4 border-blue-600 shadow-lg",
                    ),
                    class_name="hidden md:flex justify-center items-center md:w-1/3",
                ),
                class_name="flex flex-col md:flex-row items-center gap-12",
            ),
            class_name="container mx-auto px-4 py-20 md:py-32 text-left",
        ),
        id="about",
        class_name="w-full bg-white",
    )


def header() -> rx.Component:
    """The navigation header."""
    return rx.el.header(
        rx.el.div(
            rx.el.div(
                rx.icon("layers", class_name="h-6 w-6 text-blue-600"),
                rx.el.span("Mai", class_name="font-bold text-lg text-gray-800"),
                class_name="flex items-center gap-2",
            ),
            rx.el.nav(
                rx.foreach(
                    State.nav_links,
                    lambda link: rx.el.a(
                        link["name"],
                        href=link["href"],
                        class_name="text-gray-600 hover:text-blue-600 font-medium transition-colors",
                    ),
                ),
                class_name="hidden md:flex items-center gap-8",
            ),
            rx.el.a(
                "Email Me",
                href="mailto:maiduydungvn@gmail.com",
                class_name="hidden md:block bg-blue-100 text-blue-700 font-semibold px-4 py-2 rounded-lg hover:bg-blue-200 transition-colors",
            ),
            class_name="container mx-auto px-4 flex items-center justify-between",
        ),
        class_name="w-full h-20 sticky top-0 z-50 bg-white/80 backdrop-blur-md border-b border-gray-100 flex items-center",
    )


def service_card(service: dict) -> rx.Component:
    """A card for a single service."""
    return rx.el.div(
        rx.el.div(
            rx.icon(service["icon"], class_name="h-8 w-8 text-blue-600"),
            class_name="bg-blue-100 p-3 rounded-full mb-4 w-fit",
        ),
        rx.el.h3(service["title"], class_name="text-xl font-bold text-gray-900 mb-2"),
        rx.el.p(service["description"], class_name="text-gray-600"),
        class_name="bg-white p-6 rounded-2xl border border-gray-100 shadow-sm hover:shadow-lg transition-shadow",
    )


def services_section() -> rx.Component:
    """The services section."""
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "What I Do Best",
                    class_name="text-3xl md:text-4xl font-bold text-gray-800 tracking-tighter",
                ),
                rx.el.p(
                    "From infrastructure to insights, I deliver end-to-end data solutions.",
                    class_name="mt-4 text-lg text-gray-600 max-w-2xl mx-auto",
                ),
                class_name="text-center",
            ),
            rx.el.div(
                rx.foreach(State.services, service_card),
                class_name="mt-12 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8",
            ),
            class_name="container mx-auto px-4 py-20 md:py-28",
        ),
        id="services",
        class_name="w-full bg-gray-50",
    )


def tech_stack_section() -> rx.Component:
    """The tech stack section."""
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Tech Stack I Work With",
                    class_name="text-3xl md:text-4xl font-bold text-gray-800 tracking-tighter",
                ),
                rx.el.p(
                    "I use the right tools for the job, from battle-tested workhorses to modern, scalable tech.",
                    class_name="mt-4 text-lg text-gray-600 max-w-2xl mx-auto",
                ),
                class_name="text-center",
            ),
            rx.el.div(
                rx.foreach(
                    State.tech_stack,
                    lambda category: rx.el.div(
                        rx.el.h3(
                            category["category"],
                            class_name="text-lg font-semibold text-gray-700 mb-4",
                        ),
                        rx.el.div(
                            rx.foreach(
                                category["items"],
                                lambda item: rx.el.span(
                                    item,
                                    class_name="bg-gray-100 text-gray-700 text-sm font-medium px-3 py-1.5 rounded-lg",
                                ),
                            ),
                            class_name="flex flex-wrap gap-2",
                        ),
                        class_name="bg-white p-6 rounded-2xl border border-gray-100 shadow-sm",
                    ),
                ),
                class_name="mt-12 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8",
            ),
            class_name="container mx-auto px-4 py-20 md:py-28",
        ),
        id="stack",
        class_name="w-full bg-gray-50",
    )


def works_section() -> rx.Component:
    """The My Works section."""
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "My Works",
                    class_name="text-3xl md:text-4xl font-bold text-gray-800 tracking-tighter",
                ),
                rx.el.p(
                    "A selection of projects that showcase my skills in building production-grade data systems.",
                    class_name="mt-4 text-lg text-gray-600 max-w-2xl mx-auto",
                ),
                class_name="text-center",
            ),
            rx.el.div(
                rx.foreach(
                    State.works,
                    lambda work: rx.el.div(
                        rx.cond(
                            work.contains("image"),
                            rx.el.div(
                                rx.el.image(
                                    src=work["image"],
                                    class_name="w-full h-auto rounded-lg mb-6 cursor-pointer",
                                    on_click=lambda: State.toggle_image_dialog(
                                        work["image"]
                                    ),
                                )
                            ),
                            None,
                        ),
                        rx.el.div(
                            rx.el.h3(
                                work["title"],
                                class_name="text-xl font-bold text-gray-900",
                            ),
                            class_name="flex justify-between items-center mb-4",
                        ),
                        rx.el.p(work["summary"], class_name="text-gray-600 mb-6"),
                        rx.el.div(
                            rx.el.div(
                                rx.icon(
                                    "cpu",
                                    class_name="h-5 w-5 text-gray-400 mr-3 shrink-0",
                                ),
                                rx.el.div(
                                    rx.el.h4(
                                        "Technical Highlights",
                                        class_name="font-semibold text-gray-800 mb-2",
                                    ),
                                    rx.el.div(
                                        rx.foreach(
                                            work["highlights"],
                                            lambda item: rx.el.span(
                                                item,
                                                class_name="bg-blue-100 text-blue-800 text-xs font-medium px-2.5 py-1 rounded-full",
                                            ),
                                        ),
                                        class_name="flex flex-wrap gap-2",
                                    ),
                                    class_name="flex flex-col items-start",
                                ),
                                class_name="flex items-start",
                            ),
                            rx.el.div(
                                rx.icon(
                                    "trending-up",
                                    class_name="h-5 w-5 text-gray-400 mr-3 shrink-0",
                                ),
                                rx.el.div(
                                    rx.el.h4(
                                        "Business Impact",
                                        class_name="font-semibold text-gray-800 mb-2",
                                    ),
                                    rx.el.p(work["impact"], class_name="text-gray-600"),
                                    class_name="flex flex-col items-start",
                                ),
                                class_name="flex items-start",
                            ),
                            class_name="space-y-6",
                        ),
                        class_name="bg-white p-8 rounded-2xl border border-gray-100 shadow-sm hover:shadow-lg transition-shadow",
                    ),
                ),
                class_name="mt-12 grid grid-cols-1 lg:grid-cols-2 gap-8",
            ),
            class_name="container mx-auto px-4 py-20 md:py-28",
        ),
        id="works",
        class_name="w-full bg-gray-50",
    )


def index() -> rx.Component:
    """The main page of the portfolio."""
    return rx.el.main(
        header(),
        hero_section(),
        services_section(),
        works_section(),
        tech_stack_section(),
        why_me_section(),
        cta_section(),
        contact_section(),
        footer(),
        rx.radix.primitives.dialog.root(
            rx.radix.primitives.dialog.portal(
                rx.radix.primitives.dialog.overlay(
                    class_name="fixed inset-0 bg-black/50 backdrop-blur-sm z-40",
                    on_click=lambda: State.toggle_image_dialog(""),
                ),
                rx.radix.primitives.dialog.content(
                    rx.el.image(
                        src=State.show_dialog_for_image,
                        class_name="max-w-[80vw] max-h-[80vh] object-contain rounded-lg",
                    ),
                    rx.radix.primitives.dialog.close(
                        rx.el.button(
                            rx.icon("x", class_name="h-4 w-4"),
                            class_name="absolute top-2 right-2 rounded-full p-2 bg-white/50 hover:bg-white/75 transition-colors",
                            on_click=lambda: State.toggle_image_dialog(""),
                        )
                    ),
                    class_name="fixed top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 bg-transparent shadow-none w-auto h-auto z-50",
                ),
            ),
            open=State.show_dialog_for_image != "",
        ),
        class_name="font-['Inter'] bg-white text-gray-800",
    )


def why_me_section() -> rx.Component:
    """The 'Why Work With Me' section."""
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Why Work With Me",
                    class_name="text-3xl md:text-4xl font-bold text-gray-800 tracking-tighter",
                ),
                rx.el.p(
                    "I combine technical depth with a founder's mindset to deliver results, not just code.",
                    class_name="mt-4 text-lg text-gray-600 max-w-2xl mx-auto",
                ),
                class_name="text-center",
            ),
            rx.el.div(
                rx.foreach(
                    State.why_me,
                    lambda item: rx.el.div(
                        rx.el.div(
                            rx.icon(item["icon"], class_name="h-7 w-7 text-blue-600"),
                            class_name="bg-blue-100 p-3 rounded-full mb-4 w-fit",
                        ),
                        rx.el.h3(
                            item["title"],
                            class_name="text-lg font-bold text-gray-900 mb-2",
                        ),
                        rx.el.p(
                            item["description"], class_name="text-gray-600 text-sm"
                        ),
                        class_name="flex flex-col items-start text-left",
                    ),
                ),
                class_name="mt-12 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 text-center",
            ),
            class_name="container mx-auto px-4 py-20 md:py-28",
        ),
        id="why-me",
        class_name="w-full bg-white",
    )


def cta_section() -> rx.Component:
    """The call-to-action section for short-term projects."""
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.h2(
                        "Open for Short-Term Projects",
                        class_name="text-3xl font-bold text-gray-900 tracking-tighter",
                    ),
                    rx.el.p(
                        "You don't need a full-time hire. You need an expert who can deliver results now.",
                        class_name="mt-3 text-lg text-gray-600",
                    ),
                    rx.el.a(
                        "Let's Talk",
                        href="#contact",
                        class_name="mt-6 inline-flex items-center justify-center rounded-lg bg-blue-600 px-5 py-3 text-base font-medium text-white shadow-sm transition-colors hover:bg-blue-700",
                    ),
                    class_name="max-w-xl",
                ),
                rx.el.div(
                    rx.foreach(
                        State.project_highlights,
                        lambda item: rx.el.div(
                            rx.icon(item["icon"], class_name="h-6 w-6 text-blue-600"),
                            rx.el.div(
                                rx.el.h3(
                                    item["title"],
                                    class_name="font-semibold text-gray-800",
                                ),
                                rx.el.p(
                                    item["description"],
                                    class_name="text-sm text-gray-600",
                                ),
                                class_name="ml-4",
                            ),
                            class_name="flex items-start",
                        ),
                    ),
                    class_name="grid gap-6 sm:grid-cols-2 lg:grid-cols-1",
                ),
                class_name="grid items-center gap-12 lg:grid-cols-2",
            ),
            class_name="container mx-auto px-4 py-20 md:py-24",
        ),
        class_name="w-full bg-white",
    )


def contact_section() -> rx.Component:
    """The contact section."""
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Let's Build Something",
                    class_name="text-3xl md:text-4xl font-bold text-gray-800 tracking-tighter",
                ),
                rx.el.p(
                    "Reach out if you need a data expert who can ship results.",
                    class_name="mt-4 text-lg text-gray-600",
                ),
                class_name="text-center max-w-2xl mx-auto",
            ),
            rx.el.div(
                rx.el.a(
                    rx.icon("mail", class_name="h-5 w-5 mr-2"),
                    "Email",
                    href="mailto:maiduydungvn@gmail.com",
                    class_name="flex items-center justify-center gap-2 rounded-lg bg-gray-100 px-6 py-3 font-semibold text-gray-800 transition-colors hover:bg-gray-200",
                ),
                rx.el.a(
                    rx.icon("linkedin", class_name="h-5 w-5 mr-2"),
                    "LinkedIn",
                    href="https://www.linkedin.com/in/maiduydung/",
                    class_name="flex items-center justify-center gap-2 rounded-lg bg-gray-100 px-6 py-3 font-semibold text-gray-800 transition-colors hover:bg-gray-200",
                ),
                rx.el.a(
                    rx.icon("calendar", class_name="h-5 w-5 mr-2"),
                    "Calendly",
                    href="https://calendly.com/maiduydungvn/meeting-with-mai",
                    class_name="flex items-center justify-center gap-2 rounded-lg bg-gray-100 px-6 py-3 font-semibold text-gray-800 transition-colors hover:bg-gray-200",
                ),
                class_name="mt-12 flex flex-wrap justify-center gap-4",
            ),
            class_name="container mx-auto px-4 py-20 md:py-28",
        ),
        id="contact",
        class_name="w-full bg-gray-50",
    )


def footer() -> rx.Component:
    """The footer of the portfolio."""
    return rx.el.footer(
        rx.el.div(
            rx.el.p(
                f"© {2025} Mai. All Rights Reserved.",
                class_name="text-sm text-gray-500",
            ),
            rx.el.div(
                rx.foreach(
                    State.nav_links,
                    lambda link: rx.el.a(
                        link["name"],
                        href=link["href"],
                        class_name="text-sm text-gray-500 hover:text-blue-600 transition-colors",
                    ),
                ),
                class_name="flex items-center gap-6",
            ),
            class_name="container mx-auto flex justify-between items-center px-4",
        ),
        class_name="w-full py-8 border-t border-gray-100 bg-white",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index)