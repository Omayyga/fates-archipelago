from BaseClasses import Location

class fatesLocation(Location):
    game = "Fire Emblem Fates Revelation"

LOCATION_ID_START = 0xFEF800

location_table = {
    # >> chapter checks <M<
    "Prologue Complete": LOCATION_ID_START + 1,
    "Chapter 1 Complete": LOCATION_ID_START + 2,
    "Chapter 2 Complete": LOCATION_ID_START + 3,
    "Chapter 3 Complete": LOCATION_ID_START + 4,
    "Chapter 4 Complete": LOCATION_ID_START + 5,
    "Chapter 5 Complete": LOCATION_ID_START + 6,
    "Chapter 6 Complete": LOCATION_ID_START + 7,
    "Chapter 7 Complete": LOCATION_ID_START + 8,
    "Chapter 8 Complete": LOCATION_ID_START + 9,
    "Chapter 9 Complete": LOCATION_ID_START + 10,
    "Chapter 10 Complete": LOCATION_ID_START + 11,

    # >> chest checks <<
    "Chapter 10 Chest 1": LOCATION_ID_START + 12,
    "Chapter 10 Chest 2": LOCATION_ID_START + 13,

    # >> Shop Checks <<
    "Dawn Armory level 1 slot 1": LOCATION_ID_START + 14,
    "Rod Shop level 1 slot 1": LOCATION_ID_START + 15,

    # >> Recruitment Checks <<
    "Recruitment - Felicia": LOCATION_ID_START + 16,
}

event_locations = {
    "Defeat Anankos": None,
}

locationNameToID = {
    **location_table,
}

# >> regions used by starter progression chain
# expanded further later just an early scaffolding <<
chapter_region_order = [
    "Prologue",
    "Chapter 1",
    "Chapter 2",
    "Chapter 3",
    "Chapter 4",
    "Chapter 5",
    "Chapter 6",
    "Chapter 7",
    "Chapter 8",
    "Chapter 9",
    "Chapter 10",
    "Endgame"
]

region_locations = {
    "Prologue": [
        "Prologue Complete",
    ],
    "Chapter 1": [
        "Chapter 1 Complete",
    ],
    "Chapter 2": [
        "Chapter 2 Complete",
        "Recruitment - Felicia",
    ],
    "Chapter 3": [
        "Chapter 3 Complete",
    ],
    "Chapter 4": [
        "Chapter 4 Complete",
    ],
    "Chapter 5": [
        "Chapter 5 Complete",
    ],
    "Chapter 6": [
        "Chapter 6 Complete",
    ],
    "Chapter 7": [
        "Chapter 7 Complete",
    ],
    "Chapter 8": [
        "Chapter 8 Complete",
    ],
    "Chapter 9": [
        "Chapter 9 Complete",
    ],
    "Chapter 10": [
        "Chapter 10 Complete",
        "Chapter 10 Chest 1",
        "Chapter 10 Chest 2",
    ],
    "My Castle": [
        "Dawn Armory level 1 slot 1",
        "Rod Shop level 1 slot 1",
    ],
    "Endgame": [],
}

# >> for region access logic <<
chapter_clear_events = {
    "Prologue": "Prologue Cleared",
    "Chapter 1": "Chapter 1 Cleared",
    "Chapter 2": "Chapter 2 Cleared",
    "Chapter 3": "Chapter 3 Cleared",
    "Chapter 4": "Chapter 4 Cleared",
    "Chapter 5": "Chapter 5 Cleared",
    "Chapter 6": "Chapter 6 Cleared",
    "Chapter 7": "Chapter 7 Cleared",
    "Chapter 8": "Chapter 8 Cleared",
    "Chapter 9": "Chapter 9 Cleared",
    "Chapter 10": "Chapter 10 Cleared",
}