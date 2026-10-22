"""Layout, nav, album cards, tour table, and the mailing list."""

import reflex as rx

from cadmium_saints.data import (
    ALBUMS,
    MEMBERS,
    NAV_LINKS,
    QUOTES,
    RECORD_CHOICES,
    SHOWS,
    STATUS_LABELS,
    TICKER,
)
from cadmium_saints.state import SiteState

BACKGROUND = rx.asset("background.jpg")


def nav_link(label: str, href: str) -> rx.Component:
    """A sticky-nav link that closes the mobile menu."""
    return rx.link(
        label,
        href=href,
        on_click=SiteState.close_nav,
        class_name=rx.cond(
            SiteState.router.page.path == href,
            "nav-link is-active",
            "nav-link",
        ),
    )


def navbar() -> rx.Component:
    """Sticky top bar with the band mark and section links."""
    return rx.el.header(
        rx.el.a("Skip to content", href="#content", class_name="skip-link"),
        rx.el.div(
            rx.link(
                rx.el.span(class_name="mark"),
                rx.el.span("Cadmium Saints", class_name="brand-name"),
                href="/",
                on_click=SiteState.close_nav,
                class_name="brand",
            ),
            rx.el.button(
                rx.el.span(),
                rx.el.span(),
                rx.el.span(),
                type="button",
                class_name=rx.cond(
                    SiteState.nav_open,
                    "nav-toggle is-open",
                    "nav-toggle",
                ),
                on_click=SiteState.toggle_nav,
                aria_label="Open the menu",
            ),
            rx.el.nav(
                *[nav_link(label, href) for label, href in NAV_LINKS],
                class_name=rx.cond(SiteState.nav_open, "nav-links is-open", "nav-links"),
                aria_label="Sections",
            ),
            class_name="nav-inner",
        ),
        class_name="nav",
    )


def footer() -> rx.Component:
    """Closing bar. The band is fictional and the copy says so."""
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                rx.el.p("Cadmium Saints", class_name="footer-brand"),
                rx.el.p(
                    "A fictional band from Port Meridian. The songs, rooms, and dates on this site were made up.",
                    class_name="footer-note",
                ),
            ),
            rx.el.div(
                rx.el.p("Night Orchard Records", class_name="footer-meta"),
                rx.el.p("book@cadmiumsaints.example", class_name="footer-meta"),
                rx.el.p("© 2026 Cadmium Saints", class_name="footer-meta"),
            ),
            class_name="footer-inner",
        ),
        class_name="footer",
    )


def shell(*children) -> rx.Component:
    """Page root. The painting is applied once, here, and stays fixed."""
    return rx.box(
        navbar(),
        ticker(),
        rx.el.main(*children, id="content", class_name="page-body"),
        footer(),
        class_name="page-root",
        background_image=f"url('{BACKGROUND}')",
        background_size="cover",
        background_position="center",
        background_attachment="fixed",
        background_repeat="no-repeat",
        min_height="100vh",
    )


def ticker() -> rx.Component:
    """A full-bleed strip of record and tour words."""
    return rx.el.div(
        rx.el.div(
            rx.el.span(TICKER, class_name="ticker-item"),
            rx.el.span(TICKER, class_name="ticker-item"),
            class_name="ticker-track",
        ),
        class_name="ticker",
        aria_hidden="true",
    )


def kicker(number: str, label: str) -> rx.Component:
    """A numbered section label, offset from the panel it introduces."""
    return rx.el.div(
        rx.el.span(number, class_name="kicker-num"),
        rx.el.span(label, class_name="kicker-label"),
        class_name="kicker",
    )


def status_badge(status: str) -> rx.Component:
    """Sold-out, low-ticket, or on-sale pill."""
    return rx.el.span(STATUS_LABELS[status], class_name=f"badge badge-{status}")


def album_card(album: dict, shift: bool = False) -> rx.Component:
    """An album sleeve. The tracklist opens when the title or button is clicked."""
    opened = SiteState.open_album == album["id"]
    shift_class = " album-shift" if shift else " album-plain"
    return rx.el.article(
        rx.el.div(
            rx.el.div(
                rx.el.span(album["catalog"], class_name="sleeve-cat"),
                rx.el.span(album["year"], class_name="sleeve-year"),
                class_name="sleeve",
                background_color=album["accent"],
            ),
            rx.el.div(
                rx.el.p(album["label"], class_name="album-label"),
                rx.el.h3(
                    rx.el.button(
                        album["title"],
                        type="button",
                        class_name="album-title-btn",
                        on_click=SiteState.toggle_album(album["id"]),
                    ),
                    class_name="album-heading",
                ),
                rx.el.p(album["blurb"], class_name="album-blurb"),
                class_name="album-copy",
            ),
            rx.el.button(
                rx.cond(opened, "Close", "Tracklist"),
                rx.el.span(
                    f"{len(album['tracks'])} songs · {album['runtime']}",
                    class_name="album-runtime",
                ),
                type="button",
                class_name="track-btn",
                on_click=SiteState.toggle_album(album["id"]),
            ),
            class_name="album-top",
        ),
        rx.cond(
            opened,
            rx.el.ol(
                *[
                    rx.el.li(
                        rx.el.span(track["n"], class_name="t-n", color=album["accent"]),
                        rx.el.span(track["title"], class_name="t-title"),
                        rx.el.span(track["time"], class_name="t-time"),
                        class_name="track",
                    )
                    for track in album["tracks"]
                ],
                class_name="tracklist",
            ),
        ),
        class_name="album panel" + shift_class,
        id=album["id"],
    )


def tour_table(shows: list[dict]) -> rx.Component:
    """Date, city, room, and ticket status."""
    return rx.el.div(
        rx.el.table(
            rx.el.thead(
                rx.el.tr(
                    rx.el.th("Date"),
                    rx.el.th("City"),
                    rx.el.th("Room"),
                    rx.el.th("Tickets"),
                )
            ),
            rx.el.tbody(
                *[
                    rx.el.tr(
                        rx.el.td(show["date"], custom_attrs={"data-label": "Date"}),
                        rx.el.td(show["city"], custom_attrs={"data-label": "City"}),
                        rx.el.td(
                            rx.el.span(show["venue"], class_name="venue"),
                            rx.el.span(show["note"], class_name="venue-note"),
                            custom_attrs={"data-label": "Room"},
                        ),
                        rx.el.td(
                            status_badge(show["status"]),
                            custom_attrs={"data-label": "Tickets"},
                        ),
                        class_name=f"show-row is-{show['status']}",
                    )
                    for show in shows
                ]
            ),
            class_name="tour-table",
        ),
        class_name="table-wrap panel",
    )


def hero() -> rx.Component:
    """Band name, a short pitch, and the next room."""
    show = SHOWS[0]
    return rx.el.section(
        rx.el.p("Port Meridian  ·  est. 2017  ·  Night Orchard", class_name="eyebrow"),
        rx.el.h1(
            rx.el.span("Cadmium", class_name="line"),
            rx.el.span("Saints", class_name="line line-offset"),
            class_name="hero-title",
        ),
        rx.el.p(
            "Four people, a rented room above a chandlery, and songs that keep the windows open. Indie rock with the paint still wet.",
            class_name="lede",
        ),
        rx.el.div(
            rx.link("Index of Bruises", href="/discography", class_name="btn btn-hot"),
            rx.link("Spring dates", href="/tour", class_name="btn btn-ghost"),
            class_name="hero-actions",
        ),
        rx.el.aside(
            rx.el.p("Next room", class_name="next-kicker"),
            rx.el.p(show["date"], class_name="next-date"),
            rx.el.p(show["city"], class_name="next-city"),
            rx.el.p(show["venue"], class_name="next-venue"),
            status_badge(show["status"]),
            class_name="next-show",
        ),
        rx.el.p("Live from the east dock", class_name="vert-label"),
        class_name="hero",
    )


def manifesto() -> rx.Component:
    """Short band story and a few counts, set off-axis."""
    return rx.el.section(
        kicker("01", "The room"),
        rx.el.div(
            rx.el.div(
                rx.el.h2("Still the room above the sign shop.", class_name="section-title"),
                rx.el.p(
                    "Cadmium Saints started where the paint fumes from the chandlery came up through the floorboards. Ada writes like she is leaving a note for someone who already left. Remy plays guitar parts that sound like a window in the rain. Noah holds the floor. Ivo hits the kit like the song owes him money and also a favor.",
                    class_name="body-copy",
                ),
                rx.el.p(
                    "They still print a setlist. They still ignore half of it. Index of Bruises is the newest record, twelve songs about staying, and the spring run is how they plan to play them loud enough.",
                    class_name="body-copy",
                ),
            ),
            rx.el.ul(
                rx.el.li(rx.el.strong("2017"), rx.el.span("formed above a chandlery")),
                rx.el.li(rx.el.strong("04"), rx.el.span("records on the shelf")),
                rx.el.li(rx.el.strong("12"), rx.el.span("rooms this spring")),
                class_name="stats",
            ),
            class_name="split",
        ),
        class_name="section",
    )


def latest_record() -> rx.Component:
    """The current album, with the same expanding tracklist as the discography."""
    return rx.el.section(
        kicker("02", "Latest record"),
        rx.el.div(
            rx.el.div(
                rx.el.h2("Index of Bruises", class_name="section-title"),
                rx.el.p(
                    "Out on Night Orchard. Click the title or the tracklist button and the songs drop open.",
                    class_name="body-copy",
                ),
                rx.link("The other three records", href="/discography", class_name="text-link"),
                class_name="section-intro",
            ),
            album_card(ALBUMS[-1], shift=True),
            class_name="stack",
        ),
        class_name="section",
        id="record",
    )


def upcoming() -> rx.Component:
    """Three dates, then the door to the full table."""
    return rx.el.section(
        kicker("03", "On the road"),
        rx.el.div(
            rx.el.h2("The first three rooms.", class_name="section-title"),
            rx.el.p(
                "Glasgow and Manchester are gone. Dublin is close. The rest of the run is on the tour page, badges and all.",
                class_name="body-copy tight",
            ),
            class_name="section-intro",
        ),
        tour_table(SHOWS[:3]),
        rx.link("All twelve dates", href="/tour", class_name="text-link tour-more"),
        class_name="section",
    )


def signup_form() -> rx.Component:
    """Mailing list fields. Validation runs in SiteState.join_list."""
    return rx.el.form(
        rx.el.div(
            rx.el.label(
                rx.el.span("Name", class_name="label-text"),
                rx.el.input(
                    name="name",
                    placeholder="Ada Voss",
                    auto_complete="name",
                    max_length=80,
                    class_name="field",
                ),
                class_name="field-label",
            ),
            rx.el.label(
                rx.el.span("Email", class_name="label-text"),
                rx.el.input(
                    name="email",
                    type="email",
                    placeholder="ada@example.com",
                    auto_complete="email",
                    max_length=254,
                    class_name="field",
                ),
                class_name="field-label",
            ),
            rx.el.label(
                rx.el.span("City", class_name="label-text"),
                rx.el.input(
                    name="city",
                    placeholder="Optional, so we know the coast",
                    auto_complete="address-level2",
                    max_length=80,
                    class_name="field",
                ),
                class_name="field-label",
            ),
            rx.el.label(
                rx.el.span("What got you", class_name="label-text"),
                rx.el.select(
                    rx.el.option("Which record got you here?", value=""),
                    *[rx.el.option(choice, value=choice) for choice in RECORD_CHOICES],
                    name="record",
                    class_name="field",
                    default_value="",
                ),
                class_name="field-label",
            ),
            class_name="form-grid",
        ),
        rx.cond(
            SiteState.error != "",
            rx.el.p(SiteState.error, class_name="form-error", role="alert"),
        ),
        rx.el.button("Put me on the list", type="submit", class_name="btn btn-hot"),
        on_submit=SiteState.join_list,
        no_validate=True,
        class_name="signup-form",
    )


def signup_success() -> rx.Component:
    """Confirmation after a valid signup."""
    return rx.el.div(
        rx.el.p(
            "You're on the list, ",
            rx.el.strong(SiteState.fan_name),
            ".",
            class_name="success-lead",
        ),
        rx.cond(
            SiteState.city != "",
            rx.el.p("We'll watch ", SiteState.city, " first.", class_name="body-copy"),
            rx.el.p(
                "No city, so the next note will be whenever a song or a date is actually worth the postage.",
                class_name="body-copy",
            ),
        ),
        rx.el.p(
            "The thing that got you here: ",
            rx.el.strong(SiteState.record),
            ".",
            class_name="body-copy",
        ),
        rx.el.button(
            "Add someone else",
            type="button",
            on_click=SiteState.reset_list,
            class_name="btn btn-ghost",
        ),
        class_name="form-success",
    )


def signup() -> rx.Component:
    """Mailing-list section. Names stay in this browser session."""
    return rx.el.section(
        kicker("04", "The list"),
        rx.el.div(
            rx.el.div(
                rx.el.h2("A short list. Rare mail.", class_name="section-title"),
                rx.el.p(
                    "A note when the tour hits your coast, and a day-early link when a song is finished. No weekly letter, no merch blast, no mystery PDF.",
                    class_name="body-copy",
                ),
                rx.el.p(
                    "Names stay in this session on the machine running the app. A refresh clears them. Nothing is sent to a third party.",
                    class_name="fine-print",
                ),
            ),
            rx.cond(SiteState.joined, signup_success(), signup_form()),
            class_name="signup-layout panel",
        ),
        class_name="section",
        id="list",
    )


def page_intro(kicker_num: str, kicker_label: str, title: str, copy: str) -> rx.Component:
    """Shared top of an interior page."""
    return rx.el.section(
        kicker(kicker_num, kicker_label),
        rx.el.div(
            rx.el.h1(title, class_name="page-title"),
            rx.el.p(copy, class_name="lede lede-page"),
            class_name="intro-copy",
        ),
        class_name="section page-intro",
    )


def discography_page() -> rx.Component:
    """Every record, staggered, each with an expanding tracklist."""
    return shell(
        page_intro(
            "01",
            "Discography",
            "Four records, none of them tidy.",
            "Click a title or the tracklist button. The songs open under the sleeve and the one you had open closes.",
        ),
        rx.el.div(
            *[album_card(album, shift=index % 2 == 1) for index, album in enumerate(ALBUMS)],
            class_name="album-stack",
        ),
    )


def tour_page() -> rx.Component:
    """Full spring run with sold-out badges."""
    return shell(
        page_intro(
            "02",
            "Tour",
            "Index of Bruises, on the floor.",
            "Twelve rooms, March 2027. Sold out means sold out. Low tickets means go this week. Doors are at seven unless a room says otherwise, and the band is on at nine.",
        ),
        tour_table(SHOWS),
        rx.el.section(
            rx.el.div(
                rx.el.h2("Before you come.", class_name="section-title"),
                rx.el.ul(
                    rx.el.li("Support is local and announced the week of the show."),
                    rx.el.li("The set is Index of Bruises plus two songs they still argue about."),
                    rx.el.li("No professional cameras. Phones at chest height, please."),
                    rx.el.li("Ages follow the room. Amsterdam is the all-ages exception."),
                    class_name="notes",
                ),
                class_name="panel notes-panel",
            ),
            class_name="section",
        ),
    )


def member_card(member: dict) -> rx.Component:
    """One person, a monogram, and the sentence they stand by."""
    return rx.el.article(
        rx.el.div(member["mark"], class_name="monogram", color=member["accent"]),
        rx.el.p(member["role"], class_name="member-role"),
        rx.el.h2(member["name"], class_name="member-name"),
        rx.el.p(member["bio"], class_name="body-copy"),
        rx.el.blockquote(
            member["quote"],
            class_name="member-quote",
            border_left=f"3px solid {member['accent']}",
        ),
        class_name="member panel",
        border_top=f"4px solid {member['accent']}",
    )


def band_page() -> rx.Component:
    """Four profiles and three press lines."""
    return shell(
        page_intro(
            "03",
            "The band",
            "Four people. One bad habit of staying late.",
            "Ada sings and writes. Remy plays guitar and keeps the tape. Noah is the floor. Ivo is early on purpose.",
        ),
        rx.el.div(
            *[member_card(member) for member in MEMBERS],
            class_name="members",
        ),
        rx.el.section(
            kicker("04", "In print"),
            rx.el.div(
                *[
                    rx.el.blockquote(
                        rx.el.p(quote["text"]),
                        rx.el.footer(quote["source"]),
                        class_name="press-quote panel",
                    )
                    for quote in QUOTES
                ],
                class_name="press",
            ),
            class_name="section",
        ),
    )


def home_page() -> rx.Component:
    """Hero, story, current record, a few dates, and the list."""
    return shell(
        hero(),
        manifesto(),
        latest_record(),
        upcoming(),
        signup(),
    )
