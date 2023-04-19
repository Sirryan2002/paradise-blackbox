import numpy as np
import matplotlib.pyplot as plt
import round_data

def blackbox_histogram(rounds, data_key, kwargs):
    bb_data = np.array([])
    for round in rounds:
        round: round_data.RoundData
        np.append(bb_data, round.get_data(data_key))
    plt.hist( **kwargs)
