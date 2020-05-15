import chr_init_param
import unittest

# Extract shift jisz unit tests

class extract_shift_jisz_unit_tests(unittest.TestCase):
    def setUp(self):
        self.extract_shift_jisz_instance = chr_init_param.extract_shift_jisz
        return super().setUp()
    def tearDown(self):
        return super().tearDown()
    
class is_shift_jisz(extract_shift_jisz_unit_tests):
    def runTest(self):
        content = b'hello\x00' # need thex \x00 otherwise inf loop
        assert self.extract_shift_jisz_instance(content, 0) == 'hello', \
            "Expected: b'hello'"

if __name__ == "__main__":
    unittest.main()