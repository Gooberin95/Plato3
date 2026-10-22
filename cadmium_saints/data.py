"""Catalog, tour, and lineup for Cadmium Saints.

The band, the songs, and the dates are fictional.
"""

ALBUMS: list[dict] = [
    {
        "id": "first-light-theft",
        "title": "First Light Theft",
        "year": "2018",
        "label": "Self-released",
        "catalog": "CS-001",
        "accent": "#3ce7ff",
        "runtime": "29:41",
        "blurb": "A debut recorded between shifts, mostly at night, mostly too hot. The chandlery downstairs left paint in the choruses.",
        "tracks": [
            {"n": "01", "title": "Chandlery", "time": "3:22"},
            {"n": "02", "title": "East Dock", "time": "2:58"},
            {"n": "03", "title": "First Light", "time": "4:11"},
            {"n": "04", "title": "Theft", "time": "3:04"},
            {"n": "05", "title": "Salt on the Neck", "time": "3:41"},
            {"n": "06", "title": "The Room Above", "time": "4:36"},
            {"n": "07", "title": "Leave the Amp On", "time": "2:47"},
            {"n": "08", "title": "Meridian", "time": "5:02"},
        ],
    },
    {
        "id": "kitchen-psalm",
        "title": "Kitchen Psalm",
        "year": "2020",
        "label": "Night Orchard",
        "catalog": "CS-004",
        "accent": "#ffe14a",
        "runtime": "37:08",
        "blurb": "Songs written in a kitchen that never had a working clock. The arguments are real. The clock still isn't.",
        "tracks": [
            {"n": "01", "title": "Psalm for the Kettle", "time": "3:18"},
            {"n": "02", "title": "Two Chairs", "time": "3:55"},
            {"n": "03", "title": "Borrowed Sugar", "time": "2:44"},
            {"n": "04", "title": "The Argument", "time": "4:21"},
            {"n": "05", "title": "Yellow Stair", "time": "3:33"},
            {"n": "06", "title": "After the Shouting", "time": "4:02"},
            {"n": "07", "title": "Coat on the Door", "time": "3:12"},
            {"n": "08", "title": "Night Orchard", "time": "3:48"},
            {"n": "09", "title": "Soft Alarm", "time": "2:59"},
            {"n": "10", "title": "Stay Until the Pan Cools", "time": "5:16"},
        ],
    },
    {
        "id": "saint-of-small-fires",
        "title": "Saint of Small Fires",
        "year": "2022",
        "label": "Night Orchard",
        "catalog": "CS-007",
        "accent": "#ff7a18",
        "runtime": "38:33",
        "blurb": "The record that got them out of the kitchen and into other people's rooms. Still smells faintly of matches.",
        "tracks": [
            {"n": "01", "title": "Small Fires", "time": "3:27"},
            {"n": "02", "title": "Matchbook", "time": "2:51"},
            {"n": "03", "title": "Saint of the Service Elevator", "time": "4:08"},
            {"n": "04", "title": "Halo, Kind Of", "time": "3:44"},
            {"n": "05", "title": "Nobody's Porch", "time": "3:19"},
            {"n": "06", "title": "Red Wire", "time": "4:40"},
            {"n": "07", "title": "The Late Room", "time": "3:06"},
            {"n": "08", "title": "Gasoline Lullaby", "time": "3:58"},
            {"n": "09", "title": "Window Tax", "time": "2:37"},
            {"n": "10", "title": "Port Meridian", "time": "4:55"},
            {"n": "11", "title": "Embers", "time": "1:48"},
        ],
    },
    {
        "id": "index-of-bruises",
        "title": "Index of Bruises",
        "year": "2025",
        "label": "Night Orchard",
        "catalog": "CS-011",
        "accent": "#ff2d55",
        "runtime": "46:06",
        "blurb": "Twelve songs about staying. The newest one, and the one they are taking on the road.",
        "tracks": [
            {"n": "01", "title": "Index", "time": "3:09"},
            {"n": "02", "title": "Bruise No. 4", "time": "3:46"},
            {"n": "03", "title": "Neon Dock", "time": "4:02"},
            {"n": "04", "title": "Ada's Bridge", "time": "3:21"},
            {"n": "05", "title": "Low Room", "time": "2:55"},
            {"n": "06", "title": "Cable", "time": "4:18"},
            {"n": "07", "title": "The Saints Go Quiet", "time": "3:33"},
            {"n": "08", "title": "Paint on Your Hands", "time": "3:14"},
            {"n": "09", "title": "Tuesday Amplifier", "time": "4:27"},
            {"n": "10", "title": "Don't Call It a Hymn", "time": "3:08"},
            {"n": "11", "title": "Harbor Nothing", "time": "4:51"},
            {"n": "12", "title": "Stay for the Last Bus", "time": "5:22"},
        ],
    },
]

SHOWS: list[dict] = [
    {
        "date": "06 Mar 2027",
        "city": "Glasgow",
        "venue": "King Tut's Wah Wah Hut",
        "status": "sold-out",
        "note": "Support announced Monday",
    },
    {
        "date": "08 Mar 2027",
        "city": "Manchester",
        "venue": "The Deaf Institute",
        "status": "sold-out",
        "note": "Matinee added, also gone",
    },
    {
        "date": "10 Mar 2027",
        "city": "Dublin",
        "venue": "Whelan's",
        "status": "low",
        "note": "Upstairs room",
    },
    {
        "date": "12 Mar 2027",
        "city": "London",
        "venue": "The Dome, Tufnell Park",
        "status": "on-sale",
        "note": "Doors 7, band at 9",
    },
    {
        "date": "15 Mar 2027",
        "city": "Paris",
        "venue": "La Maroquinerie",
        "status": "on-sale",
        "note": "Seated balcony, standing floor",
    },
    {
        "date": "17 Mar 2027",
        "city": "Brussels",
        "venue": "Botanique, Orangerie",
        "status": "sold-out",
        "note": "No re-entry",
    },
    {
        "date": "19 Mar 2027",
        "city": "Amsterdam",
        "venue": "Paradiso Noord",
        "status": "on-sale",
        "note": "All ages with a guardian",
    },
    {
        "date": "21 Mar 2027",
        "city": "Hamburg",
        "venue": "Molotow",
        "status": "on-sale",
        "note": "Club show, short set",
    },
    {
        "date": "23 Mar 2027",
        "city": "Berlin",
        "venue": "Lido",
        "status": "low",
        "note": "Late load-in, on time anyway",
    },
    {
        "date": "25 Mar 2027",
        "city": "Copenhagen",
        "venue": "Hotel Cecil",
        "status": "on-sale",
        "note": "Standing only",
    },
    {
        "date": "27 Mar 2027",
        "city": "Oslo",
        "venue": "John Dee",
        "status": "on-sale",
        "note": "Support from a local three-piece",
    },
    {
        "date": "30 Mar 2027",
        "city": "Reykjavík",
        "venue": "Iðnó",
        "status": "sold-out",
        "note": "Last night of the run",
    },
]

STATUS_LABELS = {
    "sold-out": "Sold out",
    "low": "Low tickets",
    "on-sale": "On sale",
}

MEMBERS: list[dict] = [
    {
        "name": "Ada Voss",
        "role": "Vocals, guitar",
        "mark": "AV",
        "accent": "#ff7a18",
        "bio": "Writes the setlist in pencil and then sings past it. From the east dock. Refuses in-ears, which the monitor engineer has learned to treat as a personality and not a request.",
        "quote": "If the chorus is polite, it isn't finished.",
    },
    {
        "name": "Remy Cho",
        "role": "Guitar, tape loops",
        "mark": "RC",
        "accent": "#3ce7ff",
        "bio": "Builds loops out of room tone and then plays against them. Keeps a suitcase of half-dead pedals labeled with tape that no longer sticks. Says the best note on Saint of Small Fires was a mistake the tape kept.",
        "quote": "Leave the window open. The song can use the weather.",
    },
    {
        "name": "Noah Pell",
        "role": "Bass, backing vocals",
        "mark": "NP",
        "accent": "#ffe14a",
        "bio": "The one who remembers what key the song was in last Tuesday. Plays with a pick until the chorus, then fingers, like the song sat down. Collects bus tickets and never the right ones.",
        "quote": "Somebody has to be the floor.",
    },
    {
        "name": "Ivo Maren",
        "role": "Drums",
        "mark": "IM",
        "accent": "#ff2d55",
        "bio": "Hits clean and a little early, which is the whole point. Learned on a kit missing a crash and still prefers it that way. Counts the band in by nodding at Ada. There is no stick click.",
        "quote": "Early is just on time with dirt on it.",
    },
]

QUOTES: list[dict] = [
    {
        "text": "They sound like a harbor arguing with a neon sign, and the neon sign is winning.",
        "source": "Harbor Weekly",
    },
    {
        "text": "Index of Bruises is the first rock record this year that knows when to shut up.",
        "source": "The Low Room",
    },
    {
        "text": "A kitchen-table band that fills a room without sanding off the splinters.",
        "source": "Night Orchard zine",
    },
]

RECORD_CHOICES: list[str] = [album["title"] for album in ALBUMS] + ["The live show"]

NAV_LINKS: list[tuple[str, str]] = [
    ("Music", "/discography"),
    ("Tour", "/tour"),
    ("The Band", "/band"),
    ("List", "/#list"),
]

TICKER = "   ·   ".join(
    [
        "INDEX OF BRUISES  OUT NOW",
        "SPRING 2027",
        "PORT MERIDIAN",
        "NIGHT ORCHARD RECORDS",
        "CADMIUM SAINTS",
        "TWELVE SONGS ABOUT STAYING",
    ]
)
