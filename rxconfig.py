import reflex as rx

config = rx.Config(
    app_name="mai_personal_site",
    stylesheets=["/public/output.css"],
    plugins=[
        rx.plugins.TailwindV4Plugin(),
        rx.plugins.SitemapPlugin(),
    ],
)
