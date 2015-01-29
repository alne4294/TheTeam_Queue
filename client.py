#! /usr/bin/python

from httplib import HTTPConnection
import json
from entry import entry

class HelpRequests:
    def createEntryFromResponse(response):
        response_obj =json.loads(response)
        if response_obj[error]:
            return None
        return entry(response_obj[data])

    def createListOfEntryFromResponse(response):
        response_obj =json.loads(response)
        if response_obj[error]:
            return None
        return [entry(elt) for elt in response_obj[data]]

    def baseURI():
        return "http://127.0.0.1:5000"

    def handle_request(method, uri, data = None):
        conn = HTTPConnection(baseURI())
        conn.request(method, uri, data)
        res = conn.getresponse()
        return (res.status, res.reason, res.read)

    def getCurrentQueue():
        (status, reason, obj) = handle_request('GET', '/api/1.0/queue', None)
        return (status, reason, createListOfEntryFromResponse(obj))

    def getByPosition(pos):
        (status, reason, obj) = handle_request('GET', '/api/1.0/queue/pos/' + pos, None)
        return (status, reason, createEntryFromResponse(obj))

    def getById(entryId):
        (status, reason, obj) = handle_request('GET', '/api/1.0/queue/id/' + entryId, None)
        return (status, reason, createEntryFromResponse(obj))
    
    def 
