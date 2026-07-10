import unittest
from meal_generator import meet_requirement, choose_random_macro
from food import *

class Test_meal_generator(unittest.TestCase):
    def test_meet_requirement(self):
        chicken = Food.getChicken()
        allowance = 220
        result = meet_requirement(chicken, allowance)
        self.assertEqual(result, (2, 220))

    def test_random_macro_choice(self):
        chicken = Food.getChicken()
        brocolli = Food.getBrocolli()
        asparagus = Food.getAsparagus()
        beef = Food.getBeef()
        peanut_butter = Food.getPeanutButter()
        foods = [chicken, brocolli, asparagus, beef, peanut_butter]
        result = choose_random_macro(Food_type.PROTEIN, foods)
        self.assertEqual(result.food_type, Food_type.PROTEIN)