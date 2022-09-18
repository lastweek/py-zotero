#!/usr/bin/env python3
#
# Copyright (c) Yizhou Shan syzwhat@gmail.com
#

import operator
import sys
from pyzotero import zotero

#
# FIXME
# You should get the following info from Zotero website.
# e.g.
#
# library_id=6666666
# library_type='user'
# api_key='xxxxx'


library_id=xxxx
library_type='user'
api_key='xxxxxxxxxxxx'

#
# This API call will dump all the item names under a collection
# Default to a csv format.
#
def dumpItemsOfCollection(zot, col):
    collectionID=col['data']['key']
    items = zot.everything(zot.collection_items(collectionID))
    nr = 0
    for item in items:
        if item['data']['itemType'] != "attachment":
            pub = 'unknown'
            if item['data']['itemType'] == 'journalArticle':
                pub = item['data']['publicationTitle']
            if item['data']['itemType'] == 'conferencePaper':
                pub = item['data']['proceedingsTitle']

            #  print(item)
            print("[%d] %s,%s,%s" % (nr, item['data']['title'], item['data']['date'], pub))
            nr = nr + 1

#
# Update all items' type, publication title, and year within a collection.
# I use this after I add all papers from a conference.
# It is a batch operation.
#
def updateItemsOfCollection(zot, col, publication, year):
    collectionID=col['data']['key']
    items = zot.everything(zot.collection_items(collectionID))

    for item in items:
        if item['data']['itemType'] != "attachment":
            # For conference papers
            if item['data']['itemType'] == 'conferencePaper':
                item['data']['date'] = year
                item['data']['proceedingsTitle'] = publication
            # For journal articles
            if item['data']['itemType'] == 'journalArticle':
                item['data']['date'] = year
                item['data']['publicationTitle'] = publication

            # Do the update
            zot.update_item(item)

def findCollectionByName(zot, name):
    cols = zot.everything(zot.collections())
    for col in cols:
        if col['data']['name'] == name:
            return col
    return None

def dumpCollectionRecursive(zot, col, i, recursive):
    spacing=' '*i
    print("%s- %s" % (spacing, col['data']['name']), flush=True)

    if recursive == True:
        sub = zot.everything(zot.collections_sub(col['data']['key']))
        sub = sorted(sub, key=lambda i:i['data']['name'])
        for s in sub:
            dumpCollectionRecursive(zot, s, i+4, recursive)

#
# Print all directories recursively
#
def dumpAllCollections(zot):
    print("All Collections")
    cols = zot.everything(zot.collections_top())
    cols = sorted(cols, key=lambda i:i['data']['name'])
    recursive = True
    for col in cols:
        dumpCollectionRecursive(zot, col, 0, recursive=recursive)

def main():

    zot = zotero.Zotero(library_id, library_type, api_key)

    #
    # This section is used to update proceedings
    #
    #  col = findCollectionByName(zot, "06-ISCA21")
    #  if col != None:
    #      updateItemsOfCollection(zot, col, "ISCA", "2021")
    #      dumpItemsOfCollection(zot, col)
    #
    #  col = findCollectionByName(zot, "08-Security21")
    #  if col != None:
    #      updateItemsOfCollection(zot, col, "Security", "2021")
    #      dumpItemsOfCollection(zot, col)
    #
    #  col = findCollectionByName("07-ATC21")
    #  if col != None:
    #      updateItemsOfCollection(col, "ATC", "2021")
    #      dumpItemsOfCollection(col)
    #  col = findCollectionByName("07-OSDI21")
    #  if col != None:
    #      updateItemsOfCollection(col, "OSDI", "2021")
    #      dumpItemsOfCollection(col)
    #  col = findCollectionByName("08-SIGCOMM21")
    #  if col != None:
    #      updateItemsOfCollection(col, "SIGCOMM", "2021")
    #      dumpItemsOfCollection(col)

    # SOSP 2021
    #  col = findCollectionByName(zot, "10-SOSP21")
    #  if col != None:
    #      updateItemsOfCollection(zot, col, "SOSP", "2021")
    #      dumpItemsOfCollection(zot, col)

    # ATC 2022
    #  col = findCollectionByName(zot, "07-ATC22")
    #  if col != None:
    #      updateItemsOfCollection(zot, col, "ATC", "2022")
    #      dumpItemsOfCollection(zot, col)

    dumpAllCollections(zot)

if __name__ == "__main__":
    main()
