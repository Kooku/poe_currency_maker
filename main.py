import requests
import pprint
from math import log

pp = pprint.PrettyPrinter(indent=2)

# Fetch from poe.ninja api
r = requests.get('http://poe.ninja/api/Data/GetCurrencyOverview?league=Abyss')

r_json = r.json()


# Get currency data, create a map between id and names
id_to_name = {}
name_to_id = {}
for item in r_json['currencyDetails']:
    id_to_name[item['id']] = item['name']
    name_to_id[item['name']] = item['id']

# Populate graph with weights
# graph[id][id] = log(chaos_worth)
graph = {}
for item in r_json['lines']:
    cur_id = name_to_id[item['currencyTypeName']]
    graph[cur_id] = {}
    if item['pay'] is not None:
        graph[cur_id][item['pay']['pay_currency_id']] = log(item['pay']['value'])
    if item['receive'] is not None:
        graph[cur_id][item['receive']['pay_currency_id']] = log(item['receive']['value'])
