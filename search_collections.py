import json
from pprint import pprint
from operator import itemgetter
from itertools import groupby

with open('collections.json', 'r') as fp:
    collections = json.load(fp)

search_str = "Pao"
lst = []

print search_str
print "----------"
for user in collections:
    for toon in collections[user]:
        if toon["name"] == search_str:
            #print "%s,%s" % (user, toon["star"])
            #import pdb; pdb.set_trace()
            lst.append([user,toon["star"]])

lst.sort(key = itemgetter(1))
groups = groupby(lst, itemgetter(1))

pprint([{'star': k, 'users': [x[0] for x in v]} for k, v in groups])
