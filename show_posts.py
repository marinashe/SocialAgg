#!/usr/bin/env python3

import facebook
import pymongo
import sys
from pprint import pprint
import dateutil.parser
import datetime


def show_posts(date=False):
    client = pymongo.MongoClient()
    db = client.get_database('socialagg')

    pages = db.get_collection('pages')
    pages_dict = {p['id']: p for p in pages.find()}
    posts = db.get_collection('posts')
    if date:
        date = dateutil.parser.parse(date, ignoretz=True).date()
        for post in posts.find().sort('time', pymongo.DESCENDING):
            if post['time'].date() == date:
                post['page'] = pages_dict[post['page_id']]
                for x in post:
                    print(x, post[x], sep=' : ')
                print('=======================================')
    else:
        for post in posts.find().sort('time', pymongo.DESCENDING).limit(50):
            post['page'] = pages_dict[post['page_id']]
            for x in post:
                print(x, post[x], sep=' : ')
            print('=======================================')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        show_posts(sys.argv[1])
    else:
        show_posts()