
"""
 Unit tests for px2csv
"""

import unittest
import px2csv

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.test_px = open("test_data/holdings.px")

    def test_verify_cx_text(self):
        self.assertFalse(px2csv.verify_cx_text(123));
        # make sure true is returned for valid text
        px_text = self.test_px.read()
        self.assertTrue(px2csv.verify_cx_text(px_text));
        
        # false for invalid text
        self.assertFalse(px2csv.verify_cx_text(None));
        self.assertFalse(px2csv.verify_cx_text(""));
        self.assertFalse(px2csv.verify_cx_text("Gobilty gook"));

#    def test_px_to_csv(self):

if __name__ == '__main__':
    unittest.main()
