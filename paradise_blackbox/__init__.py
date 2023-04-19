
# Program purpose is to fetch paradise API data
# and to format that data into desired data structures such as CSVs, JSON
# or even presented in graphs




import matplotlib.pyplot as plt
import numpy as np





#
# Graph Configuration
#

def build_kwargs():
    return

#
# Data Display
#

def pa_histogram():
    return
### Testing


# 
# data_list = filter_by_gamemode(data_list, gamemode_whitelist = ["nuclear operatives"])



"""
gm_dict = {}
for round in data_list:
    round: RoundData
    if not round.meta_data["game_mode_result"] in gm_dict:
        gm_dict[round.meta_data["game_mode_result"]] = 0
    gm_dict[round.meta_data["game_mode_result"]] = gm_dict[round.meta_data["game_mode_result"]] + 1

for i in gm_dict:
    print(i)




round_times = {"cult win" : [], "cult loss" : []}
w_kwarg = []

for round in data_list:
    round: RoundData
    if "win" in round.meta_data["game_mode_result"]:
        round_times["cult win"].append(get_round_length_minutes(round.meta_data))
    else:
        round_times["cult loss"].append(get_round_length_minutes(round.meta_data))

w_kwarg = [np.ones_like(round_times["cult win"]) / len(round_times["cult win"]), np.ones_like(round_times["cult loss"]) / len(round_times["cult loss"])]

# np.random.rand(len(round_times), 3)
plt.hist(round_times.values(), color=['lightgreen', 'lightcoral'], label=list(round_times.keys()), bins = list(range(40, 240, 10)), weights=w_kwarg, stacked=True)
plt.xlabel('Round Length (Minutes)')
plt.ylabel('Relative Round Frequency')
plt.legend()
plt.show()

exit()
data_list = retrieve_rounds_data(list(range(34355-650, 34355)))
output = {}
for round in data_list:
    raw_data = get_raw_data(ParaDataKeys.ORE_MINED, round)
    if not raw_data == None:
        output.update(raw_data)
plt.xticks(rotation=45, ha='right')
plt.bar(list(output.keys()), output.values(), color='g')
plt.show()
"""