import unittest
from TDEE import generate_TDEE

class Test_TDEE(unittest.TestCase):

    def test_TDEE_male(self):
        result = generate_TDEE(80, 182.88, 20, "male", 3)
        self.assertEqual(result, 2864.4)

    def test_TDEE_female(self):
        result = generate_TDEE(60, 172.72, 20, "female", 3)
        self.assertEqual(result, 2198.675)