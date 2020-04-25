import chr_init_param
import unittest

class find_chr_by_id_tests(unittest.TestCase):
    def setUp(self):
        self.find_chr_by_id_instance = chr_init_param.find_chr_by_id
    def tearDown(self):
        return super().tearDown()
class find_nonexistent_char():
    def runTest(self):
        assert self.find_chr_by_id_instance('B') == False, \
            "chr id's should be numbers"

if __name__ == "__main__":
    unittest.main()