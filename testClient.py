#! /usr/bin/python

import client

a = client.HelpRequests()

print "Current length of the queue"
print len(a.getCurrentQueue()[-1])
addedEntry = a.create("A","B","C")[-1]
print "Length of the queue after an addition"
# print len(a.getCurrentQueue()[-1])
print a.getCurrentQueue()
print "The object by position"
print a.getByPosition(0)[-1]
print "The object by id"
print a.getById(addedEntry.eid)[-1]
print "Modifying the object"
addedEntry.name = "David"
addedEntry = a.modify(addedEntry)[-1]
print "Dequeue an entry"
dequeueEntry = a.create("Alpha","Bravo","Charlie")[-1]
print "Current length of the queue"
print len(a.getCurrentQueue()[-1])
print "Current Length of the queue"
print len(a.getCurrentQueue()[-1])
addedEntry = a.delete(addedEntry.eid)
print len(a.getCurrentQueue()[-1])
