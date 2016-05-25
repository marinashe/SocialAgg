#!/usr/bin/env python3

import facebook
import pymongo
import sys
import dateutil.parser


def bests():
    client = pymongo.MongoClient()
    db = client.get_database('socialagg')
    pages = db.get_collection('pages')
    posts = db.get_collection('posts')

    for page in pages.find():

        allposts = [x for x in posts.find({'page_id': page['id']})]
        print(page['name'], 'The best posts', sep='\n')
        for post in sorted(allposts, key=lambda likes: likes['likes'], reverse=True)[:3]:
            print(post['time'],'{} likes'.format(post['likes']), post['message'], sep=' ')


    print('Ok')

if __name__ == '__main__':
    bests()