

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

    def test_getByPos(self):
        entry = self.app.get('/api/1.0/queue/pos/0')
        self.assertEqual(entry.status_code, 200)

    def test_getQueue(self):
        testData = dict(name= "Justin", location= "test1", course= "compsci")
        resp = self.app.post('/api/1.0/queue', data=json.dumps(testData), content_type='application/json')
        back =  json.loads(resp.get_data())
        self.assertEqual(resp.status_code, 200)

        # assert 'No entries here so far' in entry.data
        # tester = queue.app.test_client(self)
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