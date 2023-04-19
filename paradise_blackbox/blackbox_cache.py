import round_data as rd
import blackbox_api
import json
import math
#
# Database I/O
#

import mysql.connector


def db_insert_round(round: rd.RoundData):
    sql = "INSERT INTO rounds (round_id, round_data, round_meta_data, round_player_count) VALUES (%s, %s, %s, %s)"
    val = (round.round_num, json.dumps(round.round_data), json.dumps(round.meta_data), json.dumps(round.count_data))
    if round.meta_data == None or round.round_data == None:
        if db_is_dirty_data(round.round_num):
            return # dirty data is already in DB, don't need to insert it again
        sql = "INSERT INTO data_anomalies (round_id) VALUES (%s)"
        val = [round.round_num]
    cursor = mydb.cursor()
    cursor.execute(sql, val)
    mydb.commit()

def db_retrieve_rounds(rounds = []):
    format_strings = ','.join(['%s'] * len(rounds))
    sql = "SELECT round_id, round_data, round_meta_data, round_player_count FROM rounds WHERE round_id IN (%s)" % format_strings
    val = tuple(rounds)
    cursor = mydb.cursor()
    cursor.execute(sql, val)
    rounds_to_return = []
    for round in cursor.fetchall():
        rounds_to_return.append(rd.RoundData(round[0], json.loads(round[1]), json.loads(round[2]), json.loads(round[3])))
    return rounds_to_return

def db_get_all_round_nums():
    sql = "SELECT round_id FROM rounds"
    cursor = mydb.cursor()
    cursor.execute(sql)
    print(cursor.fetchall())

def db_round_exists(round_num):
    sql = "SELECT round_id FROM rounds WHERE round_id = %s"
    val = [round_num]
    cursor = mydb.cursor()
    cursor.execute(sql, val)
    if len(cursor.fetchall()):
        return True
    return False

def db_is_dirty_data(round_num):
    sql = "SELECT round_id FROM data_anomalies WHERE round_id = %s"
    val = [round_num]
    cursor = mydb.cursor()
    cursor.execute(sql, val)
    if len(cursor.fetchall()):
        return True
    return False

#
# Data Retrieve Helpers
#

def get_round_data(round):
    round_data = blackbox_api.grab_round_data(round)
    meta_data = blackbox_api.grab_metadata(round)
    count_data = blackbox_api.grab_count_data(round)
    round_to_store = rd.RoundData(round, round_data, meta_data, count_data)
    db_insert_round(round_to_store)
    if round_to_store.round_data == None or round_to_store.meta_data == None:
        return None
    return round_to_store

def round_range(round_min, round_max):
    return list(range(round_min, round_max + 1))

def retrieve_rounds_data(rounds = []):
    if not len(rounds):
        return []
    rounds_to_grab = rounds
    data = db_retrieve_rounds(rounds)
    print(f"Retrieved {len(data)} cached rounds from database")
    for round in data:
        round: rd.RoundData
        rounds_to_grab.remove(round.round_num)
    if(len(rounds_to_grab) == 0):
        return data
    count = 0
    animation = ["[           ]","[=          ]","[===        ]",
                "[====       ]","[=====      ]","[======     ]",
                "[=======    ]","[========   ]","[=========  ]",
                "[========== ]","[===========]"]
    round_grab_count = len(rounds_to_grab) / (len(animation) - 1)
    print(f"Retrieving round data from Blackbox API")
    for round_num in rounds_to_grab:
        count = count + 1
        if(db_is_dirty_data(round_num)):
            continue
        print(animation[math.floor(count / round_grab_count)], f"{count}/{len(rounds_to_grab)} Rounds", end = '\r')
        round_to_append = get_round_data(round_num)
        if round_to_append:
            data.append(round_to_append)
    print(f"Succesfully Grabbed {len(rounds)} Rounds")
    return data
