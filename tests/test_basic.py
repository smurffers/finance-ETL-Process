import src
import unittest

class BasicTestSuite(unittest.TestCase):
    """ Class for basic testing"""

    def test_first_file(self):
        self.assertEqual(src.test_method(), "Hello")


if __name__ == '__main__':
    unittest.main()