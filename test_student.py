import unittest
from proj2 import *

class TestsForEachFunction(unittest.TestCase):
    def setUp(self):
        self.data = read_csv_lines("ben_test_data.csv")

    def test_listlen_empty(self):
        self.assertEqual(listlen(None), 0)



if __name__ == "__main__":
    unittest.main()
