import round_data
import numpy as np
#
# Data Filterng
#

def filter_by_gamemode(data, gamemode_whitelist = [], split = False):
    if(not split and not len(gamemode_whitelist)):
        return data
    if split:
        filtered_list = {}
    else:
        filtered_list = []
    for round in data:
        round: round_data.RoundData
        if not len(gamemode_whitelist) or round.meta_data["game_mode"] in gamemode_whitelist:
            if split:
                if not round.meta_data["game_mode"] in filtered_list:
                    filtered_list[round.meta_data["game_mode"]] = []
                filtered_list[round.meta_data["game_mode"]].append(round)
            else:
                filtered_list.append(round)
    return filtered_list

def filter_by_map(data, map_whitelist = [], split = False):
    if(not split and not len(map_whitelist)):
        return data
    if split:
        filtered_list = {}
    else:
        filtered_list = []
    for round in data:
        round: round_data.RoundData
        if not len(map_whitelist) or round.meta_data["map_name"] in map_whitelist:
            if split:
                if not round.meta_data["map_name"] in filtered_list:
                    filtered_list[round.meta_data["map_name"]] = []
                filtered_list[round.meta_data["map_name"]].append(round)
            else:
                filtered_list.append(round)
    return filtered_list

def filter_by_round_length(data, length_min, length_max):
    if(not length_min and not length_min):
        return data
    if not length_min:
        length_min = 0
    filtered_list = []
    for round in data:
        round: round_data.RoundData
        if round.round_length >= length_min or round.round_length <= length_max:
            filtered_list.append(round)
    return filtered_list

def filter_by_avg_player_count(data, count_min, count_max):
    if(not count_min and not count_max):
        return data
    if not count_min:
        count_min = 0
    filtered_list = []
    for round_info in data:
        round_info: round_data.RoundData
        player_avg = round(np.average(list(round_info.st_player_count.values())))
        if player_avg >= count_min or player_avg <= count_max:
            filtered_list.append(round_info)
    return filtered_list

def filter_by_gamemode_result(data, result_whitelist = [], split = False):
    if(not split and not len(result_whitelist)):
        return data
    if split:
        filtered_list = {}
    else:
        filtered_list = []
    for round in data:
        round: round_data.RoundData
        if not len(result_whitelist) or round.meta_data["game_mode_result"] in result_whitelist:
            if split:
                if not round.meta_data["game_mode_result"] in filtered_list:
                    filtered_list[round.meta_data["game_mode_result"]] = []
                filtered_list[round.meta_data["game_mode_result"]].append(round)
            else:
                filtered_list.append(round)
    return filtered_list


def split_by_period(rounds, period):

    match period:
        case "days":
            None
        case "weeks":
            None
        case "months":
            None
        case "quarters":
            None
        case "half-years":
            None
        case "years":
            None