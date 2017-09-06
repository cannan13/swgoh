#!/usr/bin/env python

from bs4 import BeautifulSoup
import urllib2
import json

# Get guild members
url = 'https://swgoh.gg/g/5743/force-a-fide/'

req = urllib2.Request(url, headers={'User-Agent': 'Wget/1.17.1'})
r = urllib2.urlopen(req).read()
soup = BeautifulSoup(r, 'html.parser')

with open('members.txt') as f:
    members = f.readlines()
members = [x.strip() for x in members]

# retrieve profiles from swgoh.gg
profiles = {}

for link in soup.find_all('a'):
    if (link.get('href').startswith('/u/')):
        profiles[link.text.strip()] = link.get('href')

for member in members:
    if ( member not in profiles ):
        print "%s has no profile" % member

for profile in profiles:
    if ( profile not in members ):
        print "%s shows a profile, not in guild" % profile

#with open('profiles.txt', 'w') as p:
#    for profile in profiles:
#        p.write(profile + '\n')

# retrieve collections for each guild member
collections = {}

for user in profiles:
    profile_url = profiles[user]
    user_collection = []

    url = 'http://swgoh.gg%scollection/' % profile_url

    req = urllib2.Request(url, headers={'User-Agent': 'Wget/1.17.1'})
    r = urllib2.urlopen(req).read()
    soup = BeautifulSoup(r, 'html.parser')

    for link in soup.find_all("a", "char-portrait-full-link"):
        for div in link.find_all("div", "char-portrait-full-level"):
            level = str(div.contents[0])
        for div in link.find_all("div", "char-portrait-full-gear-level"):
            gear = str(div.contents[0])
        for div in link.select("[class~=star]"):
            if len(div["class"]) < 3:
                star = div["class"][1]
        toon = {"name": link.img["alt"], "level": level, "gear": gear, "star": star}
        user_collection.append(toon)
    for link in soup.find_all("a", "char-portrait-link"):
        toon = {"name": link.img["alt"], "star": 'Inactive'}
        user_collection.append(toon)

    collections[user] = user_collection

with open('collections.json', 'w') as fp:
    json.dump(collections, fp)
    
