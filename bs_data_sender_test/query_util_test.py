__author__ = 'archmagece'

import unittest

import bs_data_sender.query_util

class MyTestCase(unittest.TestCase):
    def test_something(self):
        json = {
            "aaa": "aaa",
            "bbb": "bbb"
        }
        result = bs_data_sender.query_util.generate_insert_query_by_dict("tbl1", json)
        print result
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
