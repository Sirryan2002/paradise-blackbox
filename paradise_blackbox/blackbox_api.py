import requests
#
# API Functions
#

def build_api(_round_num):
    return "https://api.paradisestation.org/stats/blackbox/{round_num}".format(round_num = _round_num)

def build_meta_api(_round_num):
    return "https://api.paradisestation.org/stats/metadata/{round_num}".format(round_num = _round_num)

def build_count_api(_round_num):
    return "https://api.paradisestation.org/stats/playercounts/{round_num}".format(round_num = _round_num)

def grab_metadata(_round):
    meta_api_link = build_meta_api(_round)
    meta_response = requests.get(meta_api_link.format(round = _round))
    try:
        return meta_response.json()
    except:
        return

def grab_round_data(_round):
    api_link = build_api(_round)
    response = requests.get(api_link.format(round = _round))
    try:
        return response.json()
    except:
        return

def grab_count_data(_round):
    api_link = build_count_api(_round)
    response = requests.get(api_link.format(round = _round))
    try:
        return response.json()
    except:
        return