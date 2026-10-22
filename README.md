# Cadmium Saints

A site for **Cadmium Saints**, a fictional indie rock band from Port Meridian. It is built with [Reflex](https://reflex.dev/) 0.10.0.

The painting behind every page lives in `assets/background.jpg` and is applied once on the page root, with `background_size="cover"`, `background_position="center"`, and `background_attachment="fixed"`. It stays locked while you scroll. The hero, record sleeves, tour table, member profiles, and mailing list sit on translucent dark panels so the canvas still shows through.

## Python version

This project targets **Python 3.14.4**.

Current Reflex (0.10.0) supports Python 3.14. The package requires `Python >=3.11,<4.0`, lists 3.14 in its classifiers, and added 3.14 compatibility in Reflex 0.8.15. `.python-version` is `3.14.4`.

## Run it on Ubuntu

`python3` on Ubuntu is often older than 3.14. Install **Python 3.14.4** first, then clone and run the app.

### Install Python 3.14.4

[uv](https://docs.astral.sh/uv/) installs that exact version without root:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source "$HOME/.local/bin/env"
uv python install 3.14.4
mkdir -p "$HOME/.local/bin"
ln -sfn "$(uv python find 3.14.4)" "$HOME/.local/bin/python3.14"
python3.14 --version
```

`python3.14 --version` should print `Python 3.14.4`.

### Clone, install, and run

```bash
git clone https://github.com/Gooberin95/Plato3.git
cd Plato3
python3.14 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
reflex run
```

`reflex init` is not required. This repo already has `rxconfig.py`, the `cadmium_saints` package, and `assets/`. Run it only if those files are missing:

```bash
reflex init
```

If Reflex offers to overwrite `rxconfig.py` or the app package, keep the copies from the repo.

The first `reflex run` downloads the frontend toolchain and compiles the site. When the terminal says the app is ready, open:

**http://localhost:3000**

Reflex also starts an API on port 8000. The site itself is the frontend on port 3000. Stop it with Ctrl+C.

## What's on the site

- `/` — hero, the band in short, the latest record, three tour dates, and the mailing list
- `/discography` — album cards; click a title or **Tracklist** to open the songs
- `/tour` — the spring 2027 table, with sold-out badges
- `/band` — Ada Voss, Remy Cho, Noah Pell, and Ivo Maren

The mailing list checks the name, email, optional city, and record choice in Reflex state. A valid signup stays in that browser session. Refreshing the page clears it.
