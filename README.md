# Python Scripts to interact with Zotero

I'm using [pyzotero](https://github.com/urschrei/pyzotero).

Some functions I built:

Dump all your collections (folders) recursively
```python
def dumpAllCollections(zot):
```

Find a collection reference by name
```python
def findCollectionByName(zot, name):
```

Dump all items within a collection
```python
def dumpItemsOfCollection(zot, col):
```

Update the `publication` and `year` fields of all items within a collection.
You can probably derive more useful functions from it.
```python
def updateItemsOfCollection(zot, col, publication, year):
```

