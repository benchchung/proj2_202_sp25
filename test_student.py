import unittest
from proj2 import *

class TestsForEachFunction(unittest.TestCase):
    def setUp(self):
        self.data = read_csv_lines("ben_test_data.csv")



    def test_listlen_empty(self):
        self.assertEqual(listlen(None), 0)

    def test_listlen_file(self):
        self.assertEqual(listlen(self.data), 6)

    def test_filterrows_country(self):
        expected = Node(Row("Vietnam", 2022, 150.0, 1.52, 300.0, 3.05, 350.0, 3.55))
        self.assertEqual(filter_rows(self.data, "country", "equal", "Vietnam"), expected)

    def test_parsing_rows_with_nones(self):
        fields = ["India", "2019", "", "", "", "", "", ""]
        result =parse_row(fields)
        self.assertEqual(result.electricity_and_heat_co2_emissions, None)

    def test_csv_reading(self):
        self.assertEqual(read_csv_lines("data_with_wrong_header.csv"), None)

if __name__ == "__main__":
    unittest.main()
