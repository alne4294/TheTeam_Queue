

import os
import main
import unittest
import tempfile
import json
from time import sleep
from httplib import HTTPConnection

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, main.app.config['DATABASE'] = tempfile.mkstemp()
        main.app.config['TESTING'] = True
        self.app = main.app.test_client()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(main.app.config['DATABASE'])

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
        print jsonEntry
        self.assertEqual(jsonEntry['data'], [])
        self.assertEqual(entry.status_code, 200)

if __name__ == '__main__':
    unittest.main()