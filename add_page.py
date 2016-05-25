#!/usr/bin/env python3

import facebook
import pymongo
import sys


def add_page_to_db(name):
    client = pymongo.MongoClient()
    db = client.get_database('socialagg')
    pages = db.get_collection('pages')
    pages.create_index('id', unique=True)

    with open("TOKEN.txt") as f:
        TOKEN = f.read().strip()

    graph = facebook.GraphAPI(access_token=TOKEN, version='2.5')
    inf = graph.get_object(name,
                         fields="about,name,fan_count,picture.width(180).height(180)")

    pages.insert({'id': inf['id'],
                'name': inf['name'],
                'about': inf['about'],
                'fans': inf['fan_count'],
                'photo': inf['picture']['data']['url']})
    print('OK, added id #{} with {} fans.'.format(inf['id'], inf['fan_count']))
if __name__ == '__main__':
    add_page_to_db(sys.argv[1])