import _command_line as command_line
import argparse


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command", required=False)

# DataTypes
subparsers.add_parser("blackbox-cats", help="Display all available blackbox data keys to use.")
datacat_parser = subparsers.add_parser("metadata-cats", help="Display all available meta data keys to use.")
datacat_parser.add_argument("type", help="Show key categories.", nargs='?')
datacat_parser.add_argument("find", help="The category of keys to find", nargs='?')
metadata_parser = subparsers.add_parser("meta-data", help="Display the meta data of a specific round.")
metadata_parser.add_argument("round", help="The round number for the round info you want.")
keydata_parser = subparsers.add_parser("key-data", help="Display the blackbox key-data of a specific round.")
keydata_parser.add_argument("round", help="The round number for the round info you want.")
keydata_parser.add_argument("key", help="The blackbox key associated with the type of blackbox info you want.")
grabber_parser = subparsers.add_parser("grab-rounds", help="Ensure all rounds in this range are cached locally.")
grabber_parser.add_argument("round_min", help="Min round number in range.")
grabber_parser.add_argument("round_max", help="Max round number in range.")
meta_stat_parser = subparsers.add_parser("meta-stats", help="Meta data 1 var stats.")
meta_stat_parser.add_argument("round_min", help="Min round number in range.")
meta_stat_parser.add_argument("round_max", help="Max round number in range.")
meta_stat_parser.add_argument("key", help="Type of meta data to get stats on.")
#hello_parser = subparsers.add_parser("hello", help="Say hello.")
#hello_parser.add_argument("name", help="Who to greet.")

args = parser.parse_args()

if args.command == "blackbox-cats":
    command_line.display_all_keys()
elif args.command == "metadata-cats":
    command_line.display_meta_categories(args.type)
elif args.command == "meta-data":
    command_line.display_round_meta_data(int(args.round))
elif args.command == "key-data":
    command_line.display_round_key_data(int(args.round), str(args.key))
elif args.command == "grab-rounds":
    command_line.grab_rounds(list(range(int(args.round_min), int(args.round_max) + 1)))
elif args.command == "meta-stats":
    command_line.meta_var_stats(int(args.round_min), int(args.round_max), args.key)
else:
    raise NotImplementedError(
        f"Command {args.command} does not exist.",
    )

exit()
import round_data
import blackbox_cache
data_list =  blackbox_cache.retrieve_rounds_data(list(range(34355-2150, 32915)))
gm_dict = {}
for round in data_list:
    round: round_data.RoundData
    if not round.meta_data["end_state"] in gm_dict:
        gm_dict[round.meta_data["end_state"]] = 0
    gm_dict[round.meta_data["end_state"]] = gm_dict[round.meta_data["end_state"]] + 1

for i in gm_dict:
    print(i, ":", gm_dict[i])