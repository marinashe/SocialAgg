#!/usr/bin/env python3

import facebook
import pymongo
import sys
import dateutil.parser

from pprint import pprint




def bests():
    client = pymongo.MongoClient()
    db = client.get_database('socialagg')
    pages = db.get_collection('pages')
    posts = db.get_collection('posts')

    with open("TOKEN.txt") as f:
        TOKEN = f.read().strip()

    graph = facebook.GraphAPI(access_token=TOKEN, version='2.5')

    for page in pages.find():
        best = []
        max1 = 0
        max2 = 0
        max3 = 0
        allposts = [x for x in posts.find({'id': page['id']})][0]['posts']
        print(page['name'], 'The best posts', sep='\n')
        for post in sorted(allposts, key=lambda likes: likes[3], reverse=True)[:3]:
            print(post[0],'{} likes'.format(post[3]), post[1], sep=' ')


    print('Ok')

if __name__ == '__main__':
    bests()