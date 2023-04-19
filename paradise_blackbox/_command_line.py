import blackbox_datatypes
import blackbox_cache
import stat_helpers
import round_data
import numpy as np
from enum import Enum

def display_all_keys():
    keys_by_type = blackbox_datatypes.BlackboxDataKeys._member_map_
    print("--- All Blackbox MetaData Keys---")
    print("ENUM_NAME => \'data_key\'")
    for category in keys_by_type.keys():
        print(category)

def display_meta_categories(category):
    match category:
        case None:
            print("Available Categories: gamemodes, maps")
        case "gamemodes":
            gamemodes = blackbox_datatypes.ParadiseGamemodes._member_map_
            print("--- All Blackbox MetaData (gamemodes) Keys---")
            print("ENUM_NAME => \'data_key\'")
            for mode in gamemodes.keys():
                print(mode, "=>", f"\'{gamemodes[mode].value}\'")
        case "maps":
            maps = blackbox_datatypes.ParadiseMaps._member_map_
            print("--- All Blackbox MetaData (maps) Keys---")
            print("ENUM_NAME => \'data_key\'")
            for mode in maps.keys():
                print(mode, "=>", f"\'{maps[mode].value}\'")

def display_round_meta_data(round_num):
    round_info: round_data.RoundData = blackbox_cache.retrieve_rounds_data([round_num])[0]
    player_count = list(round_info.st_player_count.values())
    print(f"""
========== Info for Round #{round_info.round_num} ===========
    Map =>                {round_info.meta_data["map_name"]}
    Gamemode =>           {round_info.meta_data["game_mode"]}
    End Result =>         {round_info.meta_data["game_mode_result"]}
    Round Length =>       {round(round_info.round_length, 1)} Minutes
    Round-Init =>         {round_info.format_timestamp(round_info.meta_data["init_datetime"])}
    Round-Shutdown =>     {round_info.format_timestamp(round_info.meta_data["shutdown_datetime"])}
    Plyr Count (Avg) =>   {round(np.average(player_count), 1)}
    Plyr Count (Start) => {player_count[0]}
    Plyr Count (End) =>   {player_count.pop()}
============================================
    """)

def display_round_key_data(round_num, key):
    rounds = blackbox_cache.retrieve_rounds_data([round_num])
    if not len(rounds):
        print(f"No data could be found for Round #{round_num}")
        return
    round: round_data.RoundData = rounds[0]
    key = blackbox_datatypes.BlackboxDataKeys[key]
    if not key:
        raise ValueError(f"Key {key} could not be found, please double check that you're using a proper blackbox data key.")
    key_type = ""
          
    key_data = round.get_data(key)
    if not key_data:
        print(f"No data could be found for Round #{round_num} with the provided data key")
        return
    for block in round.round_data:
        if(block["key_name"] == key.value):
            key_type = block["key_type"]  
    content = ""
    match key_type:
        case "amount":
            content = f"Amount => {key_data}"
        case "text":
            content = f"text => {key_data}"
        case "tally":
            for item in key_data:
                content += f"--> {item} : {key_data[item]}\n"
        case "associative":
            for i in list(range(1, len(key_data) + 1)):
                content += f"\n<| #{i} |>\n"
                for item in key_data[str(i)]:
                    content += f"--> {item} : {key_data[str(i)][item]}\n"
        case "nested tally":
            for item in key_data:
                print(type(int))
                if type(key_data[item]) == type(int()):                
                    content += f"-> {item} : {key_data[item]}\n"
                    continue
                content += f"-> {item}\n"
                for val in key_data[item]:
                    content += f"  |-> {val} : {key_data[item][val]}\n"


    print(f"""
====== Key Info for Round #{round.round_num} =======
Key => {key} ('{key.value}')
KeyType => {key_type}
{content}
========================================
    """)

def grab_rounds(rounds):
    blackbox_cache.retrieve_rounds_data(rounds)

def meta_var_stats(round_min, round_max, key):
    rounds = blackbox_cache.retrieve_rounds_data(blackbox_cache.round_range(round_min, round_max))
    shit = stat_helpers.calculate_meta_stats(rounds, key)
    content = ""
    for i in shit:
       content += f"{i} => {shit[i]}\n"
    print(f"""
=========== 1 Var Stat Info ============
Rounds => {round_min} to {round_max}
Key => {key}
-----
{content}
========================================
    """)

def round_var_stats(rounds, stat_type):
    data = blackbox_cache.retrieve_rounds_data(rounds)


