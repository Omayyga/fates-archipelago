from BaseClasses import Item, ItemClassification

class fatesItem(Item):
    game = "Fire Emblem Fates Revelation"

ITEM_ID_START = 0xFEF000
# >> starting pool to build skeleton <<
item_table = {
    "Iron Sword": {
        "id": ITEM_ID_START + 1,
        "classification": ItemClassification.filler,
    },
    "Steel Sword": {
        "id": ITEM_ID_START + 2,
        "classification": ItemClassification.filler,
    },
    "Killer Lance": {
        "id": ITEM_ID_START + 3,
        "classification": ItemClassification.useful,
    },
    "Dragonstone": {
        "id": ITEM_ID_START + 4,
        "classification": ItemClassification.useful,
    },
    "Heal": {
        "id": ITEM_ID_START + 5,
        "classification": ItemClassification.filler,
    },
    "Master Seal": {
        "id": ITEM_ID_START + 6,
        "classification": ItemClassification.useful,
    },
    "Heart Seal": {
        "id": ITEM_ID_START + 7,
        "classification": ItemClassification.useful,
    },
    "1000G": {
        "id": ITEM_ID_START + 8,
        "classification": ItemClassification.filler,
    },
    "5000G": {
        "id": ITEM_ID_START + 9,
        "classification": ItemClassification.useful,
    },
}

itemNameToID = {
    itemName: itemData["id"] 
    for itemName, itemData in item_table.items()
}

itemNameGroups = {
    "Weapons": {
        "Iron Sword",
        "Steel Sword",
        "Killer Lance",
        "Dragonstone",
    },
    "Seals": {
        "Master Seal",
        "Heart Seal",
    },
    "Gold": {
        "1000G",
        "5000G",
    },
}