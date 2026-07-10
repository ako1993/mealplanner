from food import *
import random

def generate_meals(calorie_allowance:int):
    protein_requirement = calorie_allowance * 0.33
    carb_requirement = calorie_allowance * 0.33
    fat_requirement = calorie_allowance * 0.10
    macro_total = protein_requirement + carb_requirement + fat_requirement
    micro_requirement = calorie_allowance = macro_total


    chicken = Food.getChicken()
    brown_rice = Food.getBrownRice()
    avacado = Food.getAvacado()
    brocolli = Food.getBrocolli()
    beef = Food.getBeef()
    sweet_potato = Food.getSweetPotato()
    peanut_butter = Food.getPeanutButter()
    asparagus = Food.getAsparagus()

    food_options = [chicken, brown_rice, avacado, brocolli, beef, sweet_potato, peanut_butter, asparagus]

    calories_per_meal = calorie_allowance/3

    meal_1 = []
    meal_2 = []
    meal_3 = []


def meet_requirement(food:Food, allowance:int)->int:
    calories_from_food = 0
    servings = 0
    while(calories_from_food < allowance):
        calories_from_food += food.calories
        servings += 1
    print(f"You can have {servings} servings of {food.name} for {calories_from_food} calories")
    return servings, calories_from_food


def choose_random_macro(macro_type:Food_type, foods:list[Food])->Food:
    num = random.randint(0, len(foods)-1)
    current_food = foods[num]
    while current_food.food_type != macro_type:
        if current_food.food_type != macro_type:
            continue
        else:
            break
    print(f"The chosen food is {current_food.name} because it is a {current_food.food_type}")
    return current_food
    
    
    
    
    
