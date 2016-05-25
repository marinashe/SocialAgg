#!/usr/bin/env python3

import facebook
import pymongo
import sys
from pprint import pprint


def show_pages():
    client = pymongo.MongoClient()
    db = client.get_database('socialagg')

    pages = db.get_collection('pages')

    for page in pages.find():
        for x in page:
            print(x, page[x], sep=' : ')
        print('=======================================')

if __name__ == '__main__':
    show_pages()