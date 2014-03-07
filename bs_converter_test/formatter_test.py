__author__ = 'archmagece'

import unittest

import bs_converter.formatter


class MyTestCase(unittest.TestCase):
    def test_num2formatted_str_normal(self):
        result = bs_converter.formatter.num2formatted_str(34, 6)
        print "===="
        print result
        print "===="
        self.assertEqual(True, False)

    def test_num2formatted_str_number_error(self):
        result = bs_converter.formatter.num2formatted_str(34, -2)
        print "===="
        print result
        print "===="
        #self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
