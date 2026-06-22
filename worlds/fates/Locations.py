from BaseClasses import Location

class fatesLocation(Location):
    game = "Fire Emblem Fates Revelation"

LOCATION_ID_START = 0xFEF800

location_table = {
    # >> chapter checks <<
    "Prologue Complete": {
         "code": LOCATION_ID_START + 1,
         "region": "Prologue",
         "type": "Chapter",
    },
    "Chapter 1 Complete": {
         "code": LOCATION_ID_START + 2,
         "region": "Chapter 1",
         "type": "Chapter",
    },
    "Chapter 2 Complete": {
         "code": LOCATION_ID_START + 3,
         "region": "Chapter 2",
         "type": "Chapter",
    },
    "Chapter 3 Complete": {
         "code": LOCATION_ID_START + 4,
         "region": "Chapter 3",
         "type": "Chapter",
    },
    "Chapter 4 Complete": {
         "code": LOCATION_ID_START + 5,
         "region": "Chapter 4",
         "type": "Chapter",
    },
    "Chapter 5 Complete": {
         "code": LOCATION_ID_START + 6,
         "region": "Chapter 5",
         "type": "Chapter",
    },
    "Chapter 6 Complete": {
         "code": LOCATION_ID_START + 7,
         "region": "Chapter 6",
         "type": "Chapter",
    },
    "Chapter 7 Complete": {
         "code": LOCATION_ID_START + 8,
         "region": "Chapter 7",
         "type": "Chapter",
    },
    "Chapter 8 Complete": {
         "code": LOCATION_ID_START + 9,
         "region": "Chapter 8",
         "type": "Chapter",
    },
    "Chapter 9 Complete": {
         "code": LOCATION_ID_START + 10,
         "region": "Chapter 9",
         "type": "Chapter",
    },
    "Chapter 10 Complete": {
         "code": LOCATION_ID_START + 11,
         "region": "Chapter 10",
         "type": "Chapter",
    },
    "Chapter 11 Complete": {
          "code": LOCATION_ID_START + 17,
          "region": "Chapter 11",
          "type": "Chapter",
     },
     "Chapter 12 Complete": {
          "code": LOCATION_ID_START + 18,
          "region": "Chapter 12",
          "type": "Chapter",
     },
     "Chapter 13 Complete": {
          "code": LOCATION_ID_START + 19,
          "region": "Chapter 13",
          "type": "Chapter",
     },
     "Chapter 14 Complete": {
          "code": LOCATION_ID_START + 20,
          "region": "Chapter 14",
          "type": "Chapter",
     },
     "Chapter 15 Complete": {
          "code": LOCATION_ID_START + 21,
          "region": "Chapter 15",
          "type": "Chapter",
     },
     "Chapter 16 Complete": {
          "code": LOCATION_ID_START + 22,
          "region": "Chapter 16",
          "type": "Chapter",
     },
     "Chapter 17 Complete": {
          "code": LOCATION_ID_START + 23,
          "region": "Chapter 17",
          "type": "Chapter",
     },
     "Chapter 18 Complete": {
          "code": LOCATION_ID_START + 24,
          "region": "Chapter 18",
          "type": "Chapter",
     },
     "Chapter 19 Complete": {
          "code": LOCATION_ID_START + 25,
          "region": "Chapter 19",
          "type": "Chapter",
     },
     "Chapter 20 Complete": {
          "code": LOCATION_ID_START + 26,
          "region": "Chapter 20",
          "type": "Chapter",
     },
     "Chapter 21 Complete": {
          "code": LOCATION_ID_START + 27,
          "region": "Chapter 21",
          "type": "Chapter",
     },
     "Chapter 22 Complete": {
          "code": LOCATION_ID_START + 28,
          "region": "Chapter 22",
          "type": "Chapter",
     },
     "Chapter 23 Complete": {
          "code": LOCATION_ID_START + 29,
          "region": "Chapter 23",
          "type": "Chapter",
     },
     "Chapter 24 Complete": {
          "code": LOCATION_ID_START + 30,
          "region": "Chapter 24",
          "type": "Chapter",
     },
     "Chapter 25 Complete": {
          "code": LOCATION_ID_START + 31,
          "region": "Chapter 25",
          "type": "Chapter",
     },
     "Chapter 26 Complete": {
          "code": LOCATION_ID_START + 32,
          "region": "Chapter 26",
          "type": "Chapter",
     },
     "Chapter 27 Complete": {
          "code": LOCATION_ID_START + 33,
          "region": "Chapter 27",
          "type": "Chapter",
     },

    # >> chest checks <<
    "Chapter 10 Chest 1": {
         "code": LOCATION_ID_START + 12,
         "region": "Chapter 10",
         "type": "Chest",
    },
    "Chapter 10 Chest 2": {
         "code": LOCATION_ID_START + 13,
         "region": "Chapter 10",
         "type": "Chest",
    },

    # >> Shop Checks <<
    "Dawn Armory level 1 slot 1": {
         "code": LOCATION_ID_START + 14,
         "region": "My Castle",
         "type": "Shop",
    },
    "Rod Shop level 1 slot 1": {
         "code": LOCATION_ID_START + 15,
         "region": "My Castle",
         "type": "Shop",
    },

    # >> Recruitment Checks <<
    "Recruitment - Felicia": {
         "code": LOCATION_ID_START + 16,
         "region": "Chapter 2",
         "type": "Recruitment",
    },
}

event_locations = {
    "Defeat Anankos": None,
}

locationNameToID = {
    location_name: location_data["code"]
    for location_name, location_data in location_table.items()
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
     "Chapter 11",
     "Chapter 12",
     "Chapter 13",
     "Chapter 14",
     "Chapter 15",
     "Chapter 16",
     "Chapter 17",
     "Chapter 18",
     "Chapter 19",
     "Chapter 20",
     "Chapter 21",
     "Chapter 22",
     "Chapter 23",
     "Chapter 24",
     "Chapter 25",
     "Chapter 26",
     "Chapter 27",
     "Endgame",
]

def build_region_locations():
    """Grouped ap locations b their assigned regions"""
    grouped_locations = {
        region_name: []
        for region_name in chapter_region_order + ["My Castle"]
    }

    for location_name, location_data in location_table.items():
        region_name = location_data["region"]

        if region_name not in grouped_locations:
            grouped_locations[region_name] = []

        grouped_locations[region_name].append(location_name)
    
    return grouped_locations

region_locations = build_region_locations()

valid_location_types = {
    "Chapter",
     "Chest",
     "Shop",
     "Recruitment",
     "MyCastle"
}

def validate_location_table() -> None:
    """Validate location metadata so any mistakes are caught early"""
    seen_codes = {}

    valid_regions = set(chapter_region_order)
    valid_regions.add("My Castle")

    for location_name, location_data in location_table.items():
          if "code" not in location_data:
               raise Exception(f"Location {location_name} is missing a code")
        
          if "region" not in location_data:
               raise Exception(f"Location {location_name} is missing a region")
        
          if "type" not in location_data:
               raise Exception(f"Location {location_name} is missing a type")

          location_code = location_data["code"]
          region_name = location_data["region"]
          location_type = location_data["type"]

          if location_code in seen_codes:
               raise Exception(f"Duplicate location code {location_code} is used by {location_name} and {seen_codes[location_code]}")
          
          seen_codes[location_code] = location_name

          if region_name not in valid_regions:
               raise Exception(f"Location {location_name} has unknown region {region_name}")
          
          if location_type not in valid_location_types:
               raise Exception(f"Location {location_name} has unknown type {location_type}")

validate_location_table()

# >> for region access logic <<
chapter_clear_events = {
    "Prologue": "Prologue: Ties That Bind Cleared",
    "Chapter 1": "Chapter 1: Nohr Cleared",
    "Chapter 2": "Chapter 2: Gift of Ganglari Cleared",
    "Chapter 3": "Chapter 3: Journey Begins Cleared",
    "Chapter 4": "Chapter 4: Hoshido Cleared",
    "Chapter 5": "Chapter 5: Mother Cleared",
    "Chapter 6": "Chapter 6: Into the Ground Cleared",
    "Chapter 7": "Chapter 7: Unspeakable World Cleared",
    "Chapter 8": "Chapter 8: Traitor's Brand Cleared",
    "Chapter 9": "Chapter 9: Wanderer Cleared",
    "Chapter 10": "Chapter 10: Voice of a God Cleared",
    "Chapter 11": "Chapter 11: Mutual Enemies Cleared",
    "Chapter 12": "Chapter 12: Frozen Sea Cleared",
    "Chapter 13": "Chapter 13: A Lost Peace Cleared",
    "Chapter 14": "Chapter 14: Orders Cleared",
    "Chapter 15": "Chapter 15: Rainbow Sage Cleared",
    "Chapter 16": "Chapter 16: White Flames Cleared",
    "Chapter 17": "Chapter 17: Black Flames Cleared",
    "Chapter 18": "Chapter 18: Veiled Kingdom Cleared",
    "Chapter 19": "Chapter 19: Hidden Strings Cleared",
    "Chapter 20": "Chapter 20: Seeds of Doubt Cleared",
    "Chapter 21": "Chapter 21: Going Forward Cleared",
    "Chapter 22": "Chapter 22: Memories Cleared",
    "Chapter 23": "Chapter 23: Arete Undone Cleared",
    "Chapter 24": "Chapter 24: Days Lost Cleared",
    "Chapter 25": "Chapter 25: Blades Drawn Cleared",
    "Chapter 26": "Chapter 26: The Vallite King Cleared",
    "Chapter 27": "Chapter 27: Hear My Cry Cleared",
}