import json
from apihelper import CommunityAPI
from dbhelper import CommunityDB


with open('settings.json') as settings_file:
    settings = json.load(settings_file)

access_token = settings['access_token']
api = CommunityAPI(access_token)
groups = settings['communities']
table = CommunityDB('subscribers.sqlite')

for group_name, group_id in groups.items():
    count = api.get_subs_count(group_id)
    table.insert(group_name, count)
