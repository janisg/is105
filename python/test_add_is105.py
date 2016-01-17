import unittest
from is105 import add

class TestAdd(unittest.TestCase):
    def setUp(self):
        pass
    def test_numbers_5_7(self):
        self.assertEqual(add(5,7), 11)
    def test_string_a_b(self):
        self.assertEqual(add('a','b'), 'ab')
        
if __name__ == '__main__':
    unittest.main()