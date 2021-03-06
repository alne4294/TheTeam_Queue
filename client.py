#! /usr/bin/python

from httplib import HTTPConnection
import json
from Entry import entry

class HelpRequests:
    def createEntryFromResponse(self, response):
        print response
        response_obj =json.loads(response)
        if response_obj["error"]:
            return None
        b = response_obj["data"]
        # print "type of b: " + str(type(b))
        # print b
        print "#################"
        # print jsonStr
        return entry(jsonStr=(b))

    def createListOfEntryFromResponse(self, response):
#        response = response.replace("\\", "")
        print " TYPE OF THIS THINNNNNG::::" + str(type(response))
        response_obj =json.loads(response)
        if response_obj["error"]:
            return None
        return [entry(jsonStr=json.loads(elt)) for elt in response_obj["data"]]

    def baseURI(self):
        return "127.0.0.1:5000"

    def handle_request(self, method, uri, data = None):
        conn = HTTPConnection(self.baseURI())
        conn.request(method, uri, data)
        res = conn.getresponse()
        return (res.status, res.reason, res.read())

    def getCurrentQueue(self):
        (status, reason, obj) = self.handle_request('GET', '/api/1.0/queue')
        # print "Get current queue" + str(status) + str(reason) + str(obj)
        return str(obj)
        # return (status, reason, self.createListOfEntryFromResponse(obj))

    def getByPosition(self, pos):
        (status, reason, obj) = self.handle_request('GET', '/api/1.0/queue/pos/' + str(pos), None)
        return (status, reason, self.createEntryFromResponse(obj))

    def getById(self, entryId):
        (status, reason, obj) = self.handle_request('GET', '/api/1.0/queue/id/' + str(entryId), None)
        return (status, reason, self.createEntryFromResponse(obj))
    
    def create(self, name, course, location):
        data = '{"name":"' + name + '", "course":"' + course + '", "location":"' + str(location) + '"}'
        (status, reason, obj) = self.handle_request('POST', '/api/1.0/queue', data)
        return (status, reason, self.createEntryFromResponse(obj))

    def delete(self, entryId):
        (status, reason, obj) = self.handle_request('DELETE', '/api/1.0/queue/id/' + str(entryId), None)
        return (status, reason, self.createEntryFromResponse(obj))

    def modify(self, entry):
        (status, reason, obj) = self.handle_request('PUT', '/api/1.0/modify', json.dumps(entry.format()))
        # print "OBBBJJJ" + str(status) + str(reason) +  str(obj)
        return (status, reason, self.createEntryFromResponse(obj))
        
