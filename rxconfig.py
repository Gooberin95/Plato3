"""Reflex configuration for the Cadmium Saints site."""

import reflex as rx

config = rx.Config(
    app_name="cadmium_saints",
    show_built_with_reflex=False,
    telemetry_enabled=False,
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.RadixThemesPlugin(
            theme=rx.theme(
                appearance="dark",
                accent_color="orange",
                gray_color="slate",
                radius="none",
                has_background=False,
            )
        ),
    ],
)
