

import os
import main as queue
import unittest
import tempfile
import json

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, queue.app.config['DATABASE'] = tempfile.mkstemp()
        queue.app.config['TESTING'] = True
        self.app = queue.app.test_client()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(queue.app.config['DATABASE'])

    #=========================================================
    #TEST EMPTY GET

    def test_getByPos(self):
        entry = self.app.get('/api/1.0/queue/pos/1')
        jsonEntry = json.loads(entry.data)
        self.assertEqual(jsonEntry['data'], "No entry at position: 1")
        self.assertEqual(entry.status_code, 200)

    def test_getById(self):
        entry = self.app.get('/api/1.0/queue/id/"12345"')
        jsonEntry = json.loads(entry.data)
        self.assertEqual(jsonEntry['data'], 'No entry at ID: "12345"')
        self.assertEqual(entry.status_code, 200)

    def test__get_getPostQueue(self):
        entry = self.app.get('/api/1.0/queue')
        self.assertEqual(entry.status_code, 200)

    #=========================================================
    #TEST POST, PUT, DELETE

    def test_post_getPostQueue(self):

        #Add a record
        testData = dict(name= "Justin", location= "test1", course= "compsci")
        resp = self.app.post('/api/1.0/queue', data=json.dumps(testData), content_type='application/json')
        back =  json.loads(resp.get_data())
        self.assertEqual(resp.status_code, 200)

        #Check that the record we just inserted exists
        entry = self.app.get('/api/1.0/queue/pos/0')
        jsonEntry = json.loads(entry.data)
        self.assertEqual(jsonEntry['data']['name'], "Justin")
        self.assertEqual(entry.status_code, 200)

        eid = jsonEntry['data']['eid']

        #Remove the record we just added
        resp = self.app.delete('/api/1.0/queue/id/'+eid, data=json.dumps(testData), content_type='application/json')
        back =  json.loads(resp.get_data())
        self.assertEqual(resp.status_code, 200)


        #Check that there are no records in the queue
        entry = self.app.get('/api/1.0/queue')
        jsonEntry = json.loads(entry.data)
        self.assertEqual(jsonEntry['data'], [])
        self.assertEqual(entry.status_code, 200)





    def test_put_modify(self):

        #Add a record
        testData = dict(name= "NAME", location= "LOCATION", course= "COURSE")
        resp = self.app.post('/api/1.0/queue', data=json.dumps(testData), content_type='application/json')
        
        jsonE = json.loads(resp.data)
        eid = jsonE["data"]["eid"]
        self.assertEqual(resp.status_code, 200)

        # #Check that the record we just inserted exists
        # entry = self.app.get('/api/1.0/queue/pos/0')
        # jsonEntry = json.loads(entry.data)
        # self.assertEqual(jsonEntry['data']['name'], "NAME")
        # self.assertEqual(entry.status_code, 200)


        # eid = jsonEntry['data']['eid']

        #Modify entry w/ eid
        modData = dict(name= "NEWNAME", location="NEWLOC", course="NEWCOURSE", eid = eid)
        modResp = self.app.put('/api/1.0/modify', data= json.dumps(modData), content_type='application/json')
        modBack = json.loads(modResp.get_data())

        self.assertEqual(modBack['data']['name'], "NEWNAME")
        self.assertEqual(modBack['data']['location'], "NEWLOC")
        self.assertEqual(modBack['data']['course'], "NEWCOURSE")

        #Remove the record we just added
        resp = self.app.delete('/api/1.0/queue/id/'+eid, data=json.dumps(testData), content_type='application/json')
        back =  json.loads(resp.get_data())
        self.assertEqual(resp.status_code, 200)


        #Check that there are no records in the queue
        # entry = self.app.get('/api/1.0/queue')
        # jsonEntry = json.loads(entry.data)
        # print jsonEntry
        # self.assertEqual(jsonEntry['data'], [])
        # self.assertEqual(entry.status_code, 200) 

if __name__ == '__main__':
    unittest.main()