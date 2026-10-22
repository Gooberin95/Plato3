"""Interactive state: open album, menu, and the mailing list."""

import re

import reflex as rx

from cadmium_saints.data import RECORD_CHOICES

_EMAIL = re.compile(
    r"^[A-Za-z0-9](?:[A-Za-z0-9._%+\-]{0,62}[A-Za-z0-9])?"
    r"@[A-Za-z0-9](?:[A-Za-z0-9\-]{0,61}[A-Za-z0-9])?"
    r"(?:\.[A-Za-z0-9](?:[A-Za-z0-9\-]{0,61}[A-Za-z0-9])?)*"
    r"\.[A-Za-z]{2,63}$"
)


def validate_signup(name: str, email: str, city: str, record: str) -> str:
    """Return an error message, or an empty string when the signup is valid."""
    name = name.strip()
    email = email.strip()
    city = city.strip()
    record = record.strip()

    if len(name) < 2 or len(name) > 80 or not any(char.isalpha() for char in name):
        return "Give us a name with at least two letters."
    if (
        len(email) > 254
        or ".." in email
        or email.startswith(".")
        or not _EMAIL.fullmatch(email)
    ):
        return "That email doesn't look usable. Try a full address, like ada@example.com."
    if city and (len(city) < 2 or len(city) > 80):
        return "If you add a city, give us the whole name."
    if record not in RECORD_CHOICES:
        return "Pick the record, or the live show, that got you here."
    return ""


class SiteState(rx.State):
    """Session state for the nav, discography, and mailing list."""

    nav_open: bool = False
    open_album: str = ""
    fan_name: str = ""
    email: str = ""
    city: str = ""
    record: str = ""
    error: str = ""
    joined: bool = False

    def toggle_nav(self):
        """Open or close the small-screen menu."""
        self.nav_open = not self.nav_open

    def close_nav(self):
        """Close the menu after a link is chosen."""
        self.nav_open = False

    def toggle_album(self, album_id: str):
        """Expand one tracklist and collapse the one that was open."""
        self.open_album = "" if self.open_album == album_id else album_id

    def join_list(self, form_data: dict):
        """Validate the mailing-list form and keep a confirmed signup in session."""
        name = str(form_data.get("name", "")).strip()
        email = str(form_data.get("email", "")).strip()
        city = str(form_data.get("city", "")).strip()
        record = str(form_data.get("record", "")).strip()
        message = validate_signup(name, email, city, record)
        if message:
            self.error = message
            self.joined = False
            return
        self.fan_name = name
        self.email = email
        self.city = city
        self.record = record
        self.error = ""
        self.joined = True

    def reset_list(self):
        """Clear the confirmation so another name can be added."""
        self.fan_name = ""
        self.email = ""
        self.city = ""
        self.record = ""
        self.error = ""
        self.joined = False
