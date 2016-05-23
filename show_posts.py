#!/usr/bin/env python3

import facebook
import pymongo
import sys
from pprint import pprint
import dateutil.parser
import datetime


def show_posts(date = False):
    client = pymongo.MongoClient()
    db = client.get_database('socialagg')

    pages = db.get_collection('pages')
    posts = db.get_collection('posts')
    if date:
        date = dateutil.parser.parse(date, ignoretz=True).date()
        print(date)
        for page in pages.find():
            print(page['name'])
            for post in [p for p in [x for x in posts.find({'id': page['id']})][0]['posts'] if p[0].date() == date]:
                print(post[0], post[1], sep=':')
    else:
        for page in pages.find():
            print(page['name'])
            for post in [x for x in posts.find({'id': page['id']})][0]['posts'][:50]:
                print(post[0], post[1], sep=':')

    print('Ok')

if __name__ == '__main__':
    show_posts()