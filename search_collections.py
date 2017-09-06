import json
from pprint import pprint

with open('collections.json', 'r') as fp:
    collections = json.load(fp)

search_str = "Pao"

print search_str
print "----------"
for user in collections:
    for toon in collections[user]:
        if toon["name"] == search_str:
            print "%s: %s" % (user, toon["star"])
