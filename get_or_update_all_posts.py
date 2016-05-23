#!/usr/bin/env python3

import facebook
import pymongo
import sys
import dateutil.parser

from pprint import pprint




def get_update():
    client = pymongo.MongoClient()
    db = client.get_database('socialagg')
    pages = db.get_collection('pages')
    posts = db.get_collection('posts')

    with open("TOKEN.txt") as f:
        TOKEN = f.read().strip()

    graph = facebook.GraphAPI(access_token=TOKEN, version='2.5')

    for page in pages.find():
        allposts = graph.get_object("{}/posts".format(page['id']), limit=100)['data']
        new_rez = sorted([[dateutil.parser.parse(p['created_time'], ignoretz=True), p['message'], p['id'], graph.get_object("{}/likes?summary=true".format(p['id']), limit=100)['summary']['total_count']] for p in allposts if 'message' in p], reverse=True)
        old_rez = [x for x in posts.find({'id': page['id']})]
        if old_rez:

            old_rez_times = [p[0] for p in old_rez[0]['posts']]
            new_rez_times = [p[0] for p in new_rez]
            new_posts = len([x for x in new_rez_times if x not in old_rez_times])
            updated_posts = len([x for x in new_rez_times if x in old_rez_times])
            removed_posts = len([x for x in old_rez_times if x not in new_rez_times])
        else:
            new_posts = len(new_rez)
            updated_posts = 0
            removed_posts = 0
        posts.update({'id': page['id']}, {'id': page['id'], 'posts': new_rez}, upsert=True)

        print('Updating page "{}"'.format(page['name']),
              'Inserted {} posts, update {} posts, removed {} posts.'.format(new_posts, updated_posts, removed_posts), sep='\n')

    print('Ok')

if __name__ == '__main__':
    get_update()