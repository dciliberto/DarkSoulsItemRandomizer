import chr_init_param
import unittest

class extract_shift_jisz_unit_tests(unittest.TestCase):
    def setUp(self):
        self.shift_jisz_instance = chr_init_param.extract_shift_jisz
    def tearDown(self):
        return super().tearDown()



if __name__ == "__main__":
    unittest.main()