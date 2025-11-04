"""Mai Duy Dung - Personal Portfolio Website"""

import reflex as rx

from .pages import home_page, skills_page, tech_page, contact_page


class State(rx.State):
    """The app state."""
    pass


# Create app instance
app = rx.App()

# Register all pages
app.add_page(
    home_page,
    route="/",
    title="Mai Duy Dung - Data/ML Engineer",
    description="Trilingual Data/ML Engineer specializing in Azure, AI systems, and data infrastructure for startups and SaaS companies.",
)

app.add_page(
    skills_page,
    route="/skills",
    title="Skills - Mai Duy Dung",
    description="What I do best: Cloud-native data infrastructure, web scraping, analytics, and applied ML & AI.",
)

app.add_page(
    tech_page,
    route="/tech",
    title="Tech Stack - Mai Duy Dung",
    description="Modern tools and frameworks I use to deliver results.",
)

app.add_page(
    contact_page,
    route="/contact",
    title="Contact - Mai Duy Dung",
    description="Let's work together. Open for short-term projects and contract work.",
)
