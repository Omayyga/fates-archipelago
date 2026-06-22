from dataclasses import dataclass
from Options import Choice, DefaultOnToggle, DeathLink, PerGameCommonOptions, Toggle

class unitRand(Choice):
    """Controls whether units are randomised by patch or randomization layer."""
    display_name = "Unit Randomization"
    option_vanilla = 0
    option_randomized = 1
    default = 1

class weaponRand(Choice):
    """Controls whether weapons are randomised by patch or randomization layer."""
    display_name = "Weapon Randomization"
    option_vanilla = 0
    option_randomized = 1
    default = 1

class chestMissSafety(Choice):
    """Controls behavior of unopened chests upon chapter completion
    - None: -> missed chests stay missed
    - remote_only -> out-world items are protected.
    - protect_progression -> out-world and local progression items are protected.
    - all -> every unopened AP chest is checked on chapter clear.
    """
    display_name = "Chest Miss Safety"
    option_none = 0
    option_remote_only = 1
    option_protect_progression = 2
    option_all = 3
    default = 2

class chestAccessMode(Choice):
    """Controls how chest access is handled when chest checks are enabled"""
    display_name = "Chest Access Mode"
    option_guaranteed = 0
    option_progression_item = 1
    option_vanilla = 2
    default = 0

class guaranteedMasterSeals(Choice):
    """Controls local guaranteed master seal availability. can keep off if playing lower diffs, but unless you want to lose your sanity, turn it on"""
    display_name = "Guaranteed Master Seals"
    option_none = 0
    option_limited = 1
    default = 1

class kanaRecruitmentCheck(Choice):
    """Controls Kana's recruitment checks. Without this, male and female kana count as different checks -> could lead to softlocks."""
    display_name = "Kana Recruitment Check"
    option_shared = 0
    default = 0

class incomingDeathLinkTarget(Choice):
    """Controls how incoming DeathLink decides target."""
    display_name = "DeathLink Target"
    option_combat_unit_else_random_deployed = 0
    default = 0

class chapterCompletionChecks(DefaultOnToggle):
    """Adds chapter completion checks."""
    display_name = "Chapter Completion Checks"

class chestChecks(DefaultOnToggle):
    """Adds chest checks."""
    display_name = "Chest Checks"

class shopChecks(DefaultOnToggle):
    """Adds shop checks."""
    display_name = "Shop Checks"

class shopUpgradeChecks(DefaultOnToggle):
    """Adds shop slot checks."""
    display_name = "Shop Upgrade Checks"

class recruitChecks(DefaultOnToggle):
    """Adds recruitment checks."""
    display_name = "Recruitment Checks"

class childUnitChecks(DefaultOnToggle):
    """Adds child unit checks."""
    display_name = "Child Unit Checks"

class MyCastleChecks(DefaultOnToggle):
    """Adds My Castle checks."""
    display_name = "My Castle Checks"

class specialClassChecks(Toggle):
    """Special class checks. probably will only do this after everything else is working"""
    display_name = "Special Class Checks"

class DLCSealsInPool(DefaultOnToggle):
    """Allows DLC seals to appear in the item pool."""
    display_name = "DLC Seals in Pool"

class releaseRemaining(DefaultOnToggle):
    """Releases remaining checks upon game completion"""
    display_name = "Release Remaining Checks"


@dataclass
class fatesOptions(PerGameCommonOptions):
    unit_Rand: unitRand
    weapon_Rand: weaponRand

    chapter_completion_checks: chapterCompletionChecks

    chest_checks: chestChecks
    chest_access_mode: chestAccessMode
    chest_miss_safety: chestMissSafety

    shop_checks: shopChecks
    shop_upgrade_checks: shopUpgradeChecks

    recruit_checks: recruitChecks
    child_unit_checks: childUnitChecks
    kana_check: kanaRecruitmentCheck

    my_castle_checks: MyCastleChecks
    special_class_checks: specialClassChecks

    guaranteed_master_seals: guaranteedMasterSeals
    dlc_seals_in_pool: DLCSealsInPool

    death_link: DeathLink
    incoming_deathlink_target: incomingDeathLinkTarget

    end_release: releaseRemaining