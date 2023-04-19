from enum import Enum

#
# Para Blackbox Data Types
#

class BlackboxDataKeys(Enum):
    CRATES = "cargo_shuttle_order"
    GUN_FIRED = "gun_fired"
    RESEARCH_LEVELS = "high_research_level"
    MANIFEST = "manifest"
    JOBS = "job_preferences"
    CONTAMINATED = "contaminated"
    PR_TMS = "testmerged_prs"
    UPLINK_ITEMS = "traitor_uplink_items_bought"
    REVIVES = "players_revived"

    # Admin Data
    ADMIN_VERBS = "admin_verb"
    ADMIN_COOKIES = "admin_cookies_spawned"
    ADMIN_SECRETS = "admin_secrets_fun_used"
    # Round Meta Stats
    ROUND_END = "round_end_stats"
    # Changeling Data
    CHANGELING_STEAL_OBJ = "changeling_objective"
    CHANGELING_GENERAL_OBJ = "changeling_steal_objective"
    CHANGELING_SUCCESS = "changeling_success"
    CHANGELING_POWERS = "changeling_powers"
    # Vampire Data
    VAMPIRE_POWERS = "vampire_powers_used"
    VAMPIRE_CLASS = "vampire_subclasses"
    # Cult Data
    CULT_SPELLS = "cult_spells_prepared"
    CULT_RUNES_SCRIBED = "runes_scribed"
    CULT_RUNES_EVOKED = "runes_invoked"
    CULT_RUNES_GHOST = "runes_invoked_with_ghost"
    GUARDIAN_PICK = "guardian_pick"
    # Traitor Data
    TRAITOR_GENERAL_OBJ = "traitor_objective"
    TRAITOR_STEAL_OBJ = "traitor_steal_objective"
    TRAITOR_SUCCESS = "traitor_success"
    # Wizard Data
    WIZARD_SPELL = "wizard_spell_learned"
    WIZARD_OBJ = "wizard_objective"
    WIZARD_SUCCESS = "wizard_success"
    # Employee Job Data
    JOB_OBJECTIVE = "employee_objective"
    JOB_SUCCESS = "employee_success"
    # Chaplain Data
    RELIGION_NAME = "religion_name"
    RELIGION_DEITY = "religion_deity"
    RELIGION_BOOK = "religion_book"
    CHAPLAIN_ROD = "chaplain_weapon"
    # Silicon/Robotics Data
    AI_CREATIONS = "ais_created"
    CYBORG_FRAMES = "cyborg_frames_built"
    CYBORG_CREATION = "cyborg_birth"
    MECHS_CREATED = "mechas_created"
    # Mining Data
    PICKAXE_USAGE = "pick_used_mining"
    ORE_MINED = "ore_mined"

    ARCADE = "arcade_status"
    HANDCUFFS = "handcuffs"

    SPELLBLADE_ENCHANTS = "spellblade_enchants"
    TOGGLE_VERBS = "toggle_verbs"
    OBJECT_CRAFTING = "object_crafted"
    EVENTS = "events"
    SLIME_CORES_HARVESTED = "slime_core_harvested"
    SLIME_CORES_USED = "slime_cores_used"
    PLANTS_HARVESTED = "food_harvested"
    LEGION_CORE = "hivelord_core"
    WISP_LANTERN = "wisp_lantern"
    WARP_CUBE = "warp_cube"
    IMMORTALITY_TALISMAN = "immortality_talisman_uses"
    XENO_EVOLUTION = "alien_growth"
    MMIS_USED = "mmis_filled"
    CYBORG_MODULE = "cyborg_modtype"
    MEGAFAUNA_KILLS = "megafauna_kills"
    PLAYER_ELITE_WIN =  "player_controlled_elite_win"
    PLAYER_ELITE_LOSS = "player_controlled_elite_loss"
    AI_ELITE_WIN =  "player_controlled_elite_loss"
    AI_ELITE_LOSS = "ai_controlled_elite_loss"
    SLIME_BABIES = "slime_babies_born"
    NEWSCASTER_CHANNELS = "newscaster_channels"
    NEWSCASTER_STORIES = "newscaster_stories"
    NEWSPAPERS_PRINTED = "newscaster_newspapers_printed"
    SM_DELAMINATION = "supermatter_delaminations"
    CHEMICAL_REACTIONS = "chemical_reaction"
    KEYCARD_AUTHS = "keycard_auths"
    SECURITY_LEVELS = "security_level_changes"
    VOTES = "votes"

class BlackBoxKeysByCategory(Enum):
    AMOUNT = [BlackboxDataKeys.CRATES, BlackboxDataKeys.AI_CREATIONS, BlackboxDataKeys.CYBORG_FRAMES, BlackboxDataKeys.CYBORG_CREATION,
                BlackboxDataKeys.ADMIN_COOKIES, BlackboxDataKeys.ADMIN_SECRETS, BlackboxDataKeys.IMMORTALITY_TALISMAN, 
                BlackboxDataKeys.MMIS_USED, BlackboxDataKeys.NEWSCASTER_CHANNELS, BlackboxDataKeys.NEWSCASTER_STORIES, 
                BlackboxDataKeys.NEWSPAPERS_PRINTED, BlackboxDataKeys.SM_DELAMINATION]
    ASSOCIATIVE = [BlackboxDataKeys.PR_TMS, BlackboxDataKeys.RESEARCH_LEVELS]
    NESTED_TALLY = [BlackboxDataKeys.MANIFEST, BlackboxDataKeys.JOBS, BlackboxDataKeys.UPLINK_ITEMS, BlackboxDataKeys.ROUND_END,
                    BlackboxDataKeys.CHANGELING_STEAL_OBJ, BlackboxDataKeys.CHANGELING_GENERAL_OBJ, BlackboxDataKeys.CULT_RUNES_EVOKED,
                    BlackboxDataKeys.CULT_RUNES_GHOST, BlackboxDataKeys.WIZARD_OBJ,  BlackboxDataKeys.JOB_OBJECTIVE, 
                    BlackboxDataKeys.SPELLBLADE_ENCHANTS, BlackboxDataKeys.CHANGELING_POWERS, BlackboxDataKeys.VAMPIRE_CLASS,
                    BlackboxDataKeys.EVENTS, BlackboxDataKeys.LEGION_CORE, BlackboxDataKeys.KEYCARD_AUTHS, BlackboxDataKeys.VOTES]
    TALLY = [BlackboxDataKeys.ADMIN_VERBS, BlackboxDataKeys.CONTAMINATED, BlackboxDataKeys.REVIVES, BlackboxDataKeys.VAMPIRE_POWERS,
                BlackboxDataKeys.CHANGELING_SUCCESS, BlackboxDataKeys.CULT_SPELLS, BlackboxDataKeys.CULT_RUNES_SCRIBED, BlackboxDataKeys.GUARDIAN_PICK,
                BlackboxDataKeys.TRAITOR_SUCCESS, BlackboxDataKeys.WIZARD_SPELL, BlackboxDataKeys.WIZARD_SUCCESS, BlackboxDataKeys.JOB_SUCCESS,
                BlackboxDataKeys.HANDCUFFS, BlackboxDataKeys.PICKAXE_USAGE, BlackboxDataKeys.ORE_MINED, BlackboxDataKeys.TOGGLE_VERBS,
                BlackboxDataKeys.OBJECT_CRAFTING, BlackboxDataKeys.SLIME_CORES_HARVESTED, BlackboxDataKeys.WISP_LANTERN, BlackboxDataKeys.WARP_CUBE,
                BlackboxDataKeys.XENO_EVOLUTION, BlackboxDataKeys.CYBORG_MODULE, BlackboxDataKeys.MEGAFAUNA_KILLS, BlackboxDataKeys.PLAYER_ELITE_WIN,
                BlackboxDataKeys.PLAYER_ELITE_LOSS, BlackboxDataKeys.AI_ELITE_LOSS, BlackboxDataKeys.AI_ELITE_WIN, BlackboxDataKeys.SLIME_BABIES,
                BlackboxDataKeys.GUN_FIRED, BlackboxDataKeys.CHEMICAL_REACTIONS, BlackboxDataKeys.SLIME_CORES_USED, BlackboxDataKeys.SECURITY_LEVELS,
                BlackboxDataKeys.CRATES]
    TEXT = [BlackboxDataKeys.RELIGION_NAME, BlackboxDataKeys.RELIGION_DEITY, BlackboxDataKeys.CHAPLAIN_ROD, BlackboxDataKeys.RELIGION_BOOK]

class ParaboxKeyCats(Enum):
    AMOUNT = "amount"
    ASSOCIATIVE = "associative"
    NESTED_TALLY = "nested_tally"
    TALLY = "tally"
    TEXT = "text"

#
# Meta Data Enums
#

class ParadiseMaps(Enum):
    BOX = "Cyberiad"
    META = "MetaStation"
    DELTA = "Delta"
    CERE = "CereStation"

class ParadiseGamemodes(Enum):
    CHANGELING = "changeling"
    VAMPIRE = "vampire"
    EXTENDED = "extended"
    TRAITOR_VAMP = "traitor+vampire"
    BLOB = "blob"
    NUKIES = "nuclear emergency"
    CULT = "cult"
    TRAITOR_CLING = "traitor+changeling"
    TRAITOR = "traitor"
    AUTO_TRAITOR = "AutoTraitor"
    WIZARD_RAGIN = " ragin' mages"
    REVOLUTION = "revolution"
    WIZARD = "wizard"
    ABDUCTORS = "abduction"

class ParadiseGamemodeResults(Enum):
    CREW_WIN = ["nuclear loss - evacuation - disk secured - syndi team dead", "raging wizard loss - wizard killed"
                "wizard loss - wizard killed", "cult loss - staff stopped the cult", "blob loss - blob eliminated", 
                "nuclear loss - evacuation - disk not secured", "nuclear loss - evacuation - disk secured"]
    CREW_LOSS = ["blob win - blob took over", "cult win - cult win", "nuclear win - syndicate nuke", ""]
    HALF_WIN = ["nuclear halfwin - syndicate nuke - did not evacuate in time", "nuclear halfwin - detonation averted"]
    ADMIN = ["admin ended"]
    UNDEFINED = [None]
    