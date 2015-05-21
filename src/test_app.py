import json
import unittest
from app import app


class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_index_response(self):
        re = self.app.get('/')
        self.assertEqual(re.status_code, 200)
        json_data = json.loads(re.data)
        self.assertIn('index', json_data)
        self.assertTrue(json_data['index'])

    def test_item_response(self):
        re = self.app.get('/item/100')
        self.assertEqual(re.status_code, 200)
        json_data = json.loads(re.data)
        self.assertIn('item', json_data)
        self.assertIn('id', json_data['item'])
        self.assertEquals(json_data['item']['id'], 100)

if __name__ == "__main__":
    unittest.main()
