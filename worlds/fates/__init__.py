from BaseClasses import ItemClassification, Region
from  worlds.AutoWorld import World

from .Items import fatesItem, itemNameGroups, itemNameToID, item_table
from .Locations import fatesLocation, event_locations, locationNameToID, location_table
from .Options import fatesOptions

class fatesWorld(World):
    """
    Archipelago world for fire emblem fates.
    (As of now a skeleton implementation for testing)
    """

    game = "Fire Emblem Fates: Revelation"
    option_dataclass = fatesOptions
    options: fatesOptions

    topology_present = True

    item_name_to_id = itemNameToID
    location_name_to_id = locationNameToID
    item_name_groups = itemNameGroups

    def create_item(self, name: str) -> fatesItem:
        item_data = item_table[name]

        return fatesItem(
            name,
            item_data["classification"],
            item_data["id"],
            self.player,
        )
    
    def create_event(self, name: str) -> fatesItem:
        """Creates generation only event item"""
        return fatesItem(
            name,
            ItemClassification.progression,
            None,
            self.player,
        )
    
    def create_regions(self) -> None:
        """Creates the starter world regions.
        As of now; all checks live in one region -> planning to split into more after (chapter, mycastle etc)"""

        menu_region = Region("Menu", self.player, self.multiworld)
        revelation_region = Region("Revelation", self.player, self.multiworld)

        # >> standard AP locations <<
        for location_name, location_id in location_table.items():
            revelation_region.locations.append(
                fatesLocation(
                    self.player,
                    location_name,
                    location_id,
                    revelation_region,
                )
            )

        # >> event locations <<
        for location_name, location_id in event_locations.items():
            revelation_region.locations.append(
                fatesLocation(
                    self.player,
                    location_name,
                    location_id,
                    revelation_region,
                )
            )

        menu_region.connect(revelation_region)

        self.multiworld.regions.append(menu_region)
        self.multiworld.regions.append(revelation_region)

    def set_rules(self) -> None:
        """Sets victory logic.
        Current flag is final boss death and it is always reachable
        To be updated to require access through chapter progressions in time."""

        victory_location = self.multiworld.get_location("Defeat Anankos", self.player)
        victory_location.place_locked_item(self.create_event("Victory"))

        self.multiworld.completion_condition[self.player] = (
            lambda state: state.has("Victory", self.player)
        )

    def getFillerItemName(self) -> str:
        """Returns a safe filler item if AP needs one"""
        return "1000G"
    
    def fillSlotData(self) -> dict:
        """
        Send simple slot data to the future fates client.
        Real client will use this later for chest/shop rules, deathlink and release"""

        return {
            "route": "revelation",
            "goal": "defeat_anankos",
            "chest_miss_safety": self.options.chestMissSafety.current_key,
            "chest_access_mode": self.options.chestAccessMode.current_key,
            "death_link": bool(self.options.death_link.value),
            "incoming_death_link_target": self.options.incoming_deathlink_target.current_key,
            "release_remaining": bool(self.options.end_release.value),
        }
