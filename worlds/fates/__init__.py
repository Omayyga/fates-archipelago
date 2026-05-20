from BaseClasses import ItemClassification, Region
from worlds.AutoWorld import World

from .Items import fatesItem, itemNameGroups, itemNameToID, item_table
from .Locations import fatesLocation, locationNameToID, location_table, chapter_clear_events, chapter_region_order, region_locations
from .Options import fatesOptions

class fatesWorld(World):
    """
    Archipelago world for fire emblem fates.
    (As of now a skeleton implementation for testing)
    """

    game = "Fire Emblem Fates Revelation"
    options_dataclass = fatesOptions
    options: fatesOptions

    topology_present = True

    item_name_to_id = itemNameToID
    location_name_to_id = locationNameToID
    item_name_groups = itemNameGroups

    def create_item(self, name: str) -> fatesItem:
        """Creates an item by name"""
        item_data = item_table[name]

        return fatesItem(
            name,
            item_data["classification"],
            item_data["id"],
            self.player,
        )
    
    def create_items(self) -> None:
        """Creates the starter world items"""
        created_items = []

        # >> add a copy of each starter item <<
        for item_name in item_table:
            created_items.append(self.create_item(item_name))

        # >> fill rest with filler <<
        normal_location_count = len(location_table)
        filler_item_name = self.get_filler_item_name()

        while len(created_items) < normal_location_count:
            created_items.append(self.create_item(filler_item_name))

        # >> temp exception if too many items <<
        if len(created_items) > normal_location_count:
            raise Exception(f"Too many items created, some will not be placed!"
            f"{len(created_items)} items created for {normal_location_count} locations.")
        
        self.multiworld.itempool += created_items
    
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
        Normal checks go to chapter/mycastle.
        generation only clear events used to model chapter progression."""

        menu_region = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu_region)

        regions = {}

        # >> create chapter and MyCastle regions <<
        all_regions_names = chapter_region_order + ["My Castle"]

        for region_name in all_regions_names:
            region = Region(region_name, self.player, self.multiworld)
            regions[region_name] = region

            # >> add normal ap checks for this region <<
            for location_name in region_locations.get(region_name, []):
                if location_name not in location_table:
                    raise Exception(f"Location {location_name} is listed in region_locations "
                                    f"but is missing from location_table"
                    )
                
                region.locations.append(
                    fatesLocation(
                        self.player,
                        location_name,
                        location_table[location_name],
                        region,
                    )
                )

            # >> chapter clera event <<
            if region_name in chapter_clear_events:
                region.add_event(
                    chapter_clear_events[region_name],
                    location_type = fatesLocation,
                    item_type = fatesItem,
                    show_in_spoiler = False,
                )

            # >> victory event <<
            if region_name == "Endgame":
                region.add_event(
                    "Defeat Anankos",
                    "Victory",
                    location_type = fatesLocation,
                    item_type = fatesItem,
                )

            self.multiworld.regions.append(region)

        # >> prologue start point <<
        menu_region.connect(regions["Prologue"])

        # >> Connect chapters in order <<
        for previous_region_name, next_region_name in zip(
            chapter_region_order,
            chapter_region_order[1:],
        ):
            required_event = chapter_clear_events[previous_region_name]

            regions[previous_region_name].connect(
                regions[next_region_name],
                rule = lambda state, event = required_event: state.has(event, self.player),
            )

        # >> MyCastle available after ch.6 <<
        regions["Chapter 6"].connect(
            regions["My Castle"],
            rule = lambda state: state.has(chapter_clear_events["Chapter 6"], self.player),
        )

    def set_rules(self) -> None:
        """Sets victory logic."""

        self.multiworld.completion_condition[self.player] = (
            lambda state: state.has("Victory", self.player)
        )

    def get_filler_item_name(self) -> str:
        """Returns a safe filler item if AP needs one"""
        return "1000G"
    
    def fill_slot_data(self) -> dict:
        """
        Send simple slot data to the future fates client.
        Real client will use this later for chest/shop rules, deathlink and release"""

        return {
            "route": "revelation",
            "goal": "defeat_anankos",
            "chest_miss_safety": self.options.chest_miss_safety.current_key,
            "chest_access_mode": self.options.chest_access_mode.current_key,
            "death_link": bool(self.options.death_link.value),
            "incoming_death_link_target": self.options.incoming_deathlink_target.current_key,
            "release_remaining": bool(self.options.end_release.value),
        }
