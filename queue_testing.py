

import os
import main
import unittest
import tempfile
import json
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
    #TEST GET

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

    def test_getPostQueue(self):
        entry = self.app.get('/api/1.0/queue')
        self.assertEqual(entry.status_code, 200)

    #=========================================================
    #TEST DELETE

    #=========================================================
    #TEST POST

    #=========================================================
    #TEST PUT

        # assert 'No entries here so far' in entry.data
        # tester = main.app.test_client(self)
        # response = tester.get('/getByPos?pos=1', content_type='application/json')
        # self.assertEqual(response.status_code, 200)
        # self.assertEqual(json.loads(response.data), {"result": 8})

    # # This test will purposely fail
    # # We are checking that 2+6 is 10
    # def test_sum_fail(self):
    #     tester = app.test_client(self)
    #     response = tester.get('/_add_numbers?a=2&b=6', content_type='application/json')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(json.loads(response.data), {"result": 10})

if __name__ == '__main__':
    unittest.main()