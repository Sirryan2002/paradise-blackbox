
from datetime import datetime
import json
#
# Data Objects
#
class RoundData:
    round_length = None
    st_player_count = {}

    def __init__(self, round_num, round_data, meta_data, count_data):
        self.round_num = round_num
        self.round_data = round_data
        self.meta_data = meta_data
        self.count_data = count_data
        if(self.meta_data):
            self.round_length = self.get_round_length_minutes()
            self.st_player_count = self.normalize_player_count()

    def get_data(self, key_type):
        if self.round_data == None:
            return {}
        for block in self.round_data:
            if(block["key_name"] == key_type.value):
                return json.loads(block["raw_data"])["data"]

    def format_timestamp(self, time_to_format):
        if time_to_format == None:
            return
        date_format_str = '%Y-%m-%dT%H:%M:%S'
        return datetime.strptime(time_to_format, date_format_str)

    def normalize_player_count(self):
        standardized_player_count = {}
        for round_time in self.count_data:
            formatted_time = self.format_timestamp(round_time) - self.format_timestamp(self.meta_data["start_datetime"])
            standardized_player_count[formatted_time.seconds / 60] = self.count_data[round_time]
        return standardized_player_count

    def get_round_length_minutes(self):
        start = self.format_timestamp(self.meta_data["start_datetime"])
        end = self.format_timestamp(self.meta_data["end_datetime"])
        if start == None or end == None:
            return 0 # Round never ended :/ ??? weird ass shit
        round_length = end - start
        return round_length.seconds / 60
