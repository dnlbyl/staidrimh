
"""
 Unit tests for px2csv
"""

import px2csv

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.px2csv = range(10)

    def test_open_cx_file(self):
        # make sure the shuffled sequence does not lose any elements

    def test_px_to_csv(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)

if __name__ == '__main__':
    unittest.main()
