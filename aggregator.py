import facebook
import pymongo
import sys
from pprint import pprint
import dateutil.parser
import datetime

def get_name(name):
    return "<h3>{}</h3>".format(name)

def get_list(list_arg):
    rezult = "<ul>"
    for li in list_arg:
        rezult += "<li>{}</li>".format(li)
    return rezult + "</ul>"

def show_posts(date = False):
    client = pymongo.MongoClient()
    db = client.get_database('socialagg')
    rezult = ''
    pages = db.get_collection('pages')
    posts = db.get_collection('posts')
    if date:
        date = dateutil.parser.parse(date, ignoretz=True).date()
        print(date)
        for page in pages.find():
            rez = []
            rezult += get_name(page['name'])
            for post in sorted([p for p in [x for x in posts.find({'id': page['id']})][0]['posts'] if p[0].date() == date], reverse=True):
                rez.append(str(post[0]) + ': ' + post[1])
            rezult += get_list(rez)
    else:
        for page in pages.find():
            rez = []
            rezult += get_name(page['name'])
            for post in sorted([x for x in posts.find({'id': page['id']})][0]['posts'], reverse=True)[:50]:
                rez.append(str(post[0]) + ': ' + post[1])
            rezult += get_list(rez)
    return rezult

def show_pages():
    rez = ''
    client = pymongo.MongoClient()
    db = client.get_database('socialagg')

    pages = db.get_collection('pages')

    for page in pages.find():
        rez += get_name(page['name']) + get_list(['About: {}'.format(page['about']), 'Fans: {}'.format(page['fans'])])

    return rez

if __name__ == '__main__':
    pass