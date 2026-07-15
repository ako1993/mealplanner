import unittest
from meal_generator import meet_requirement, choose_random_macro, generate_nutrition_facts, generate_single_meal, generate_meals, getAllFoodOptions
from food import *

class Test_meal_generator(unittest.TestCase):
    def test_meet_requirement(self):
        chicken = Food.getChicken()
        allowance = 220
        result = meet_requirement(chicken, allowance)
        self.assertEqual(result, 2)

    def test_random_macro_choice(self):
        chicken = Food.getChicken()
        brocolli = Food.getBrocolli()
        asparagus = Food.getAsparagus()
        beef = Food.getBeef()
        peanut_butter = Food.getPeanutButter()
        foods = [chicken, brocolli, asparagus, beef, peanut_butter]
        result = choose_random_macro(Food_type.PROTEIN, foods)
        self.assertEqual(result.food_type, Food_type.PROTEIN)

    def test_generate_nutrition_facts(self):
        chicken = Food.getChicken()
        calories, protein, carbs, fat = generate_nutrition_facts(chicken, 2)
        self.assertEqual(calories, 220)
        self.assertEqual(protein, 46)
        self.assertEqual(carbs, 0)
        self.assertEqual(fat, 5)

    def test_generate_single_meal(self):
            chicken = Food.getChicken()
            brown_rice = Food.getBrownRice()
            avacado = Food.getAvacado()
            brocolli = Food.getBrocolli()
            beef = Food.getBeef()
            sweet_potato = Food.getSweetPotato()
            peanut_butter = Food.getPeanutButter()
            asparagus = Food.getAsparagus()

            food_options = [chicken, brown_rice, avacado, brocolli, beef, sweet_potato, peanut_butter, asparagus]

            calories, protein, carbs, fat = generate_single_meal(800, food_options)
            assert(calories - 800) <= 2

    def test_generate_meals(self):
         generate_meals(2400)
