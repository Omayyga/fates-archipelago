from BaseClasses import Item, ItemClassification

class fatesItem(Item):
    game = "Fire Emblem Fates Revelation"

ITEM_ID_START = 0xFEF000
# >> starting pool to build skeleton <<
item_table = {
    "Bronze Sword": {
        "id": ITEM_ID_START + 1,
        "classification": ItemClassification.filler,
        "category": "Weapon",
    },
    "Iron Sword": {
        "id": ITEM_ID_START + 2,
        "classification": ItemClassification.filler,
        "category": "Weapon",
    },
    "Steel Sword": {
        "id": ITEM_ID_START + 3,
        "classification": ItemClassification.filler,
        "category": "Weapon",
    },
    "Silver Sword": {
        "id": ITEM_ID_START + 4,
        "classification": ItemClassification.useful,
        "category": "Weapon",
    },
    "Killing Edge": {
        "id": ITEM_ID_START + 5,
        "classification": ItemClassification.useful,
        "category": "Weapon",
    },
    # >> lances <<
    "Bronze Lance": {
        "id": ITEM_ID_START + 6,
        "classification": ItemClassification.filler,
        "category": "Weapon",
    },
    "Iron Lance": {
        "id": ITEM_ID_START + 7,
        "classification": ItemClassification.filler,
        "category": "Weapon",
    },
    "Steel Lance": {
        "id": ITEM_ID_START + 8,
        "classification": ItemClassification.filler,
        "category": "Weapon",
    },
    "Killer Lance": {
        "id": ITEM_ID_START + 9,
        "classification": ItemClassification.useful,
        "category": "Weapon",
    },
    "Javelin": {
        "id": ITEM_ID_START + 10,
        "classification": ItemClassification.useful,
        "category": "Weapon",
    },
    # >> axes <<
    "Bronze Axe": {
        "id": ITEM_ID_START + 11,
        "classification": ItemClassification.filler,
        "category": "Weapon",
    },
    "Iron Axe": {
        "id": ITEM_ID_START + 12,
        "classification": ItemClassification.filler,
        "category": "Weapon",
    },
    "Steel Axe": {
        "id": ITEM_ID_START + 13,
        "classification": ItemClassification.filler,
        "category": "Weapon",
    },
    "Killer Axe": {
        "id": ITEM_ID_START + 14,
        "classification": ItemClassification.useful,
        "category": "Weapon",
    },
    "Hand Axe": {
        "id": ITEM_ID_START + 15,
        "classification": ItemClassification.useful,
        "category": "Weapon",
    },
    # >> bows <<
    "Bronze Bow": {
        "id": ITEM_ID_START + 16,
        "classification": ItemClassification.filler,
        "category": "Weapon",
    },
    "Iron Bow": {
        "id": ITEM_ID_START + 17,
        "classification": ItemClassification.filler,
        "category": "Weapon",
    },
    "Steel Bow": {
        "id": ITEM_ID_START + 18,
        "classification": ItemClassification.filler,
        "category": "Weapon",
    },
    "Killer Bow": {
        "id": ITEM_ID_START + 19,
        "classification": ItemClassification.useful,
        "category": "Weapon",
    },
    # >> magic / stones <<
    "Fire": {
        "id": ITEM_ID_START + 20,
        "classification": ItemClassification.filler,
        "category": "Magic",
    },
    "Thunder": {
        "id": ITEM_ID_START + 21,
        "classification": ItemClassification.filler,
        "category": "Magic",
    },
    "Lightning": {
        "id": ITEM_ID_START + 22,
        "classification": ItemClassification.useful,
        "category": "Magic",
    },
    "Dragonstone": {
        "id": ITEM_ID_START + 23,
        "classification": ItemClassification.useful,
        "category": "Weapon",
    },
    # >> staves / rods <<
    "Heal": {
        "id": ITEM_ID_START + 24,
        "classification": ItemClassification.filler,
        "category": "Staff",
    },
    "Mend": {
        "id": ITEM_ID_START + 25,
        "classification": ItemClassification.filler,
        "category": "Staff",
    },
    "Physic": {
        "id": ITEM_ID_START + 26,
        "classification": ItemClassification.useful,
        "category": "Staff",
    },
    "Freeze": {
        "id": ITEM_ID_START + 27,
        "classification": ItemClassification.useful,
        "category": "Staff",
    },
    # >> seals <<
    "Master Seal": {
        "id": ITEM_ID_START + 28,
        "classification": ItemClassification.useful,
        "category": "Seal",
    },
    "Heart Seal": {
        "id": ITEM_ID_START + 29,
        "classification": ItemClassification.useful,
        "category": "Seal",
    },
    "Partner Seal": {
        "id": ITEM_ID_START + 30,
        "classification": ItemClassification.useful,
        "category": "Seal",
    },
    "Friendship Seal": {
        "id": ITEM_ID_START + 31,
        "classification": ItemClassification.useful,
        "category": "Seal",
    },
    "Eternal Seal": {
        "id": ITEM_ID_START + 32,
        "classification": ItemClassification.useful,
        "category": "Seal",
    },
    # >> DLC seals <<
    "Dread Scroll": {
        "id": ITEM_ID_START + 33,
        "classification": ItemClassification.useful,
        "category": "DLC Seal",
    },
    "Ebon Wing": {
        "id": ITEM_ID_START + 34,
        "classification": ItemClassification.useful,
        "category": "DLC Seal",
    },
    "Witch's Mark": {
        "id": ITEM_ID_START + 35,
        "classification": ItemClassification.useful,
        "category": "DLC Seal",
    },
    # >> stat boosters <<
    "Boots": {
        "id": ITEM_ID_START + 36,
        "classification": ItemClassification.useful,
        "category": "Stat Booster",
    },
    "Energy Drop": {
        "id": ITEM_ID_START + 37,
        "classification": ItemClassification.useful,
        "category": "Stat Booster",
    },
    "Spirit Dust": {
        "id": ITEM_ID_START + 38,
        "classification": ItemClassification.useful,
        "category": "Stat Booster",
    },
    "Speedwing": {
        "id": ITEM_ID_START + 39,
        "classification": ItemClassification.useful,
        "category": "Stat Booster",
    },
    "Dracoshield": {
        "id": ITEM_ID_START + 40,
        "classification": ItemClassification.useful,
        "category": "Stat Booster",
    },
    "Talisman": {
        "id": ITEM_ID_START + 41,
        "classification": ItemClassification.useful,
        "category": "Stat Booster",
    },
    # >> gold <<
    "1000G": {
        "id": ITEM_ID_START + 42,
        "classification": ItemClassification.filler,
        "category": "Gold",
    },
    "5000G": {
        "id": ITEM_ID_START + 43,
        "classification": ItemClassification.useful,
        "category": "Gold",
    },
    "10000G": {
        "id": ITEM_ID_START + 44,
        "classification": ItemClassification.useful,
        "category": "Gold",
    },
}

starter_item_pool = [
    "Iron Sword",
    "Steel Sword",
    "Killer Lance",
    "Dragonstone",
    "Heal",
    "Master Seal",
    "Heart Seal",
    "1000G",
    "5000G",
]

itemNameToID = {
    itemName: itemData["id"] 
    for itemName, itemData in item_table.items()
}

itemNameGroups = {
    "Weapons": {
        itemName
        for itemName, itemData in item_table.items()
        if itemData["category"] in {"Weapon", "Magic"}
    },
    "Staves": {
        itemName
        for itemName, itemData in item_table.items()
        if itemData["category"] == "Staff"
    },
    "Seals": {
        itemName
        for itemName, itemData in item_table.items()
        if itemData["category"] in {"Seal", "DLC Seal"}
    },
    "Stat Boosters": {
        itemName
        for itemName, itemData in item_table.items()
        if itemData["category"] == "Stat Booster"
    },
    "Gold": {
        itemName
        for itemName, itemData in item_table.items()
        if itemData["category"] == "Gold"
    },
}

def validate_item_table() -> None:
    seen_ids = {}

    for item_name, item_data in item_table.items():
        if "id" not in item_data:
            raise Exception(f"Item {item_name} is missing an id")
        if "classification" not in item_data:
            raise Exception(f"Item {item_name} is missing a classification")
        if "category" not in item_data:
            raise Exception(f"Item {item_name} is missing a category")

        item_id = item_data["id"]

        if item_id in seen_ids:
            raise Exception(f"Duplicate item id {item_id} is used by {item_name} and {seen_ids[item_id]}")
        
        seen_ids[item_id] = item_name

        for item_name in starter_item_pool:
            if item_name not in item_table:
                raise Exception(f"starter pool references unknown item: {item_name}")
            
validate_item_table()