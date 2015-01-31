

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

    def test_get_getPostQueue(self):
        entry = self.app.get('/api/1.0/queue')
        self.assertEqual(entry.status_code, 200)

    def test_put_modify(self):

        #Add a record
        testData = dict(name= "NAME", location= "LOCATION", course= "COURSE")
        resp = self.app.post('/api/1.0/queue', data=json.dumps(testData), content_type='application/json')
        
        jsonE = json.loads(resp.get_data())
        partTwo = json.loads(jsonE['data'])

        eid = partTwo["eid"]
        self.assertEqual(resp.status_code, 200)

        #Modify entry w/ eid
        modData = dict(name= 'NEWNAME', location='NEWLOC', course='NEWCOURSE', eid = eid)
        string = json.dumps(modData)
        modResp = self.app.put('/api/1.0/modify', data=string, content_type='application/json')
        modBack = json.loads(modResp.get_data())
        modBackData = json.loads(modBack['data'])
        self.assertEqual(modBackData['name'], "NEWNAME")
        self.assertEqual(modBackData['location'], "NEWLOC")
        self.assertEqual(modBackData['course'], "NEWCOURSE")

        #Remove the record we just added
        resp = self.app.delete('/api/1.0/queue/id/'+eid, data=json.dumps(testData), content_type='application/json')
        back =  json.loads(resp.get_data())
        self.assertEqual(resp.status_code, 200)


        #Check that there are no records in the queue
        entry = self.app.get('/api/1.0/queue')
        jsonEntry = json.loads(entry.data)
        #print jsonEntry
        self.assertEqual(jsonEntry['data'], [])
        self.assertEqual(entry.status_code, 200) 

if __name__ == '__main__':
    unittest.main()