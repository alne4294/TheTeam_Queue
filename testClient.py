#! /usr/bin/python

import client

a = client.HelpRequests()


print len(a.getCurrentQueue()[-1])
addedEntry = a.create("A","B","C")[-1]
print len(a.getCurrentQueue()[-1])
addedEntry = a.delete(addedEntry["eid"])
print len(a.getCurrentQueue()[-1])
