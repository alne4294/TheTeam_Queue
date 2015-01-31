#! /usr/bin/python

import client

a = client.HelpRequests()


print a.getCurrentQueue()
print a.create("A","B","C")
print a.getCurrentQueue()
