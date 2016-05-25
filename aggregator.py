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


def show_posts(date=False):
    client = pymongo.MongoClient()
    db = client.get_database('socialagg')
    pages = db.get_collection('pages')
    pages_dict = {p['id']: p for p in pages.find()}
    posts = db.get_collection('posts')
    # TODO: instead of using find(), use:
    #       filter = {}
    #       if date:
    #           filter['time'] = {'$gte': datetime.datetime(...), '$lt': datetime.datetime(...)}
    #       find(filter)
    if date:
        date = dateutil.parser.parse(date, ignoretz=True).date()
        for post in posts.find().sort('time', pymongo.DESCENDING):
            if post['time'].date() == date:
                post['page'] = pages_dict[post['page_id']]
                yield post
    else:
        for post in posts.find().sort('time', pymongo.DESCENDING).limit(50):
            post['page'] = pages_dict[post['page_id']]
            yield post

# def show_posts(date=False):
#     client = pymongo.MongoClient()
#     db = client.get_database('socialagg')
#     pages = db.get_collection('pages')
#     posts = db.get_collection('posts')
#     if date:
#         date = dateutil.parser.parse(date, ignoretz=True).date()
#         for page in pages.find():
#             rez = []
#             for post in sorted([p for p in [x for x in posts.find({'id': page['id']})][0]['posts'] if p[0].date() == date], reverse=True):
#                 rez.append({'time': str(post[0]), 'message': post[1]})
#             if rez:
#                 yield {'name': page['name'], 'posts': rez}
#     else:
#         for page in pages.find():
#             rez = []
#             for post in sorted([x for x in posts.find({'id': page['id']})][0]['posts'], reverse=True)[:50]:
#                 rez.append({'time': str(post[0]), 'message': post[1]})
#             if rez:
#                 yield {'name': page['name'], 'posts': rez}



def show_pages():
    client = pymongo.MongoClient()
    db = client.get_database('socialagg')

    pages = db.get_collection('pages')

    for page in pages.find():
        page['best'] = bests(page['id'])
        yield page


def bests(page_id):
    client = pymongo.MongoClient()
    db = client.get_database('socialagg')
    pages = db.get_collection('pages')
    posts = db.get_collection('posts')

    rez = []
    allposts = [x for x in posts.find({'page_id': page_id})]

    for post in sorted(allposts, key=lambda x: x['likes'], reverse=True)[:3]:
        rez.append(post)

    return rez


def get_days_range():
    client = pymongo.MongoClient()
    db = client.get_database('socialagg')
    posts = db.get_collection('posts')
    days = set([post['time'].strftime('%Y/%m/%d') for post in posts.find()])

    return min(days), max(days)



if __name__ == '__main__':
    print(all_days())
