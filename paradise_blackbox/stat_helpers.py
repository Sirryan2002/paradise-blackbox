import numpy as np
import round_data
from enum import Enum

class StatisticType(Enum):
    LOCATION = ["Mean", "Median", "Mode", "Minimum", "Maximum", "Q1", "Q3"]
    SPREAD = ["Range", "IQR", "Standard Deviation", "Variance"]

def calculate_meta_stats(rounds, key):
    vals = np.array([])
    for round in rounds:
        round: round_data.RoundData
        vals = np.append(vals, np.average(list(round.st_player_count.values())))
    return calculate_one_var_stats(vals)

def calculate_round_stats(rounds, key, key_type):
    vals = np.array()
    for round in rounds:
        round: round_data.RoundData
        round.get_data(key)

    return calculate_one_var_stats(vals)

def calculate_one_var_stats(vals):
    data_to_return = {}
    data_to_return["Mean"] = round(np.mean(vals), 2)
    data_to_return["Median"] = round(np.median(vals), 2)
    x, counts = np.unique(vals, return_counts=True) #find unique values in array along with their counts
    data_to_return["Mode"] = np.argwhere(counts == np.max(counts))
    data_to_return["Minimum"] = round(vals.min(), 2)
    data_to_return["Maximum"] = round(vals.max(), 2)
    data_to_return["Q1"] = round(np.quantile(vals, .25), 2)
    data_to_return["Q3"] = round(np.quantile(vals, .75), 2)
    data_to_return["Standard Deviation"] = round(np.std(vals), 3)
    data_to_return["Range"] = round(vals.max() - vals.min(), 2)
    data_to_return["IQR"] = round(np.quantile(vals, .75) - np.quantile(vals, .25), 2)
    data_to_return["Variance"] = round(np.var(vals), 3)
    return data_to_return


