#import necessary modules
import json
import pprint
import pandas

# open and read the previous week's data:
f_data = open("weekly_data.json", "r")

# get the data as a string
f_contents = f_data.read()
f_data.close()

# convert data from a json string to a dictionary
weekly_stable_dict = json.loads(f_contents)

# trim last week's data so we only have stable data (id, state, providers) that doesn't change
for k, v in weekly_stable_dict.items():
    v.pop('downstream_growth', None)
    v.pop('upstream_growth', None)
    v.pop('network_performance', None)

# get next week's data, convert to dictionary
data_df = pandas.read_excel('next_week.xlsx', sheet_name='SG Data')
data_df_transposed = data_df.set_index('state').transpose()
weekly_update_dict = data_df_transposed.to_dict()

pp = pprint.PrettyPrinter(indent=4)

weekly_merged_dict = {}

# merge weekly_update data into new dict
for k, v in weekly_update_dict.items():
    # get downstream growth
    downstream_growth = {}
    downstream_growth['overall'] = round(v['downstream_growth_overall'], 1)
    downstream_growth['past_week'] = round(v['downstream_growth_past_week'], 1)

    # get upstream growth
    upstream_growth = {}
    upstream_growth['overall'] = round(v['upstream_growth_overall'], 1)
    upstream_growth['past_week'] = round(v['upstream_growth_past_week'], 1)

    # get network performance data
    network_performance = {}
    network_performance['normal'] = round(v['performance_normal'], 1)
    network_performance['elevated'] = round(v['performance_elevated'], 1)
    network_performance['substantially_elevated'] = round(v['performance_substantially_elevated'], 1)
    network_performance['severely_elevated'] = round(v['performance_severely_elevated'], 1)

    # merge downstream, upstream, and network performance dicts into new dict
    weekly_merged_dict[k] = {}
    weekly_merged_dict[k]['downstream_growth'] = downstream_growth
    weekly_merged_dict[k]['upstream_growth'] = upstream_growth
    weekly_merged_dict[k]['network_performance'] = network_performance


# merge weekly_stable data into new dict
for k, v in weekly_stable_dict.items():
    weekly_merged_dict[k]['id'] = v['id']
    weekly_merged_dict[k]['name'] = v['name']
    weekly_merged_dict[k]['providers'] = v['providers']


# convert to json and write to file
weekly_merged_json = json.dumps(weekly_merged_dict)
f_merged_data = open("weekly_merged_data.json", "w")
f_merged_data.write(weekly_merged_json)
f_merged_data.close()
pp.pprint(weekly_merged_dict)
