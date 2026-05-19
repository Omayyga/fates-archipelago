from BaseClasses import Location

class fatesLocation(Location):
    game = "Fire Emblem Fates Revelation"

LOCATION_ID_START = 0xFEF800

location_table = {
    # >> chapter checks <M<
    "Chapter 7 Complete": LOCATION_ID_START + 1,
    "Chapter 8 Complete": LOCATION_ID_START + 2,
    "Chapter 9 Complete": LOCATION_ID_START + 3,
    "Chapter 10 Complete": LOCATION_ID_START + 4,

    # >> chest checks <<
    "Chapter 10 Chest 1": LOCATION_ID_START + 5,
    "Chapter 10 Chest 2": LOCATION_ID_START + 6,

    # >> Shop Checks <<
    "Dawn Armory level 1 slot 1": LOCATION_ID_START + 7,
    "Rod Shop level 1 slot 1": LOCATION_ID_START + 8,

    # >> Recruitment Checks <<
    "Recruitment - Felicia": LOCATION_ID_START + 9,
}

event_locations = {
    "Defeat Anankos": None,
}

locationNameToID = {
    **location_table,
}