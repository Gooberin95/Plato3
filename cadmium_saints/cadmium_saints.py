"""Cadmium Saints site pages."""

import reflex as rx

from cadmium_saints.components import (
    band_page,
    discography_page,
    home_page,
    tour_page,
)

app = rx.App(
    stylesheets=["/fonts.css", "/styles.css"],
    style={
        "font_family": "Outfit, sans-serif",
        "color": "#f6f1e6",
        "background_color": "transparent",
    },
    html_lang="en",
    head_components=[
        rx.el.link(rel="icon", href="/favicon.svg", type="image/svg+xml"),
        rx.el.meta(name="theme-color", content="#070b16"),
    ],
)

_PAGE_IMAGE = "/background.jpg"

app.add_page(
    home_page,
    route="/",
    title="Cadmium Saints",
    description="Cadmium Saints, a fictional indie rock band from Port Meridian. Records, tour dates, and a short mailing list.",
    image=_PAGE_IMAGE,
)
app.add_page(
    discography_page,
    route="/discography",
    title="Discography · Cadmium Saints",
    description="Four Cadmium Saints records. Open a sleeve to read the tracklist.",
    image=_PAGE_IMAGE,
)
app.add_page(
    tour_page,
    route="/tour",
    title="Tour · Cadmium Saints",
    description="Index of Bruises spring 2027 dates, with sold-out badges.",
    image=_PAGE_IMAGE,
)
app.add_page(
    band_page,
    route="/band",
    title="The Band · Cadmium Saints",
    description="Ada Voss, Remy Cho, Noah Pell, and Ivo Maren.",
    image=_PAGE_IMAGE,
)
