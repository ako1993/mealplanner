from food import *
import random

def generate_meals(calorie_allowance:int):
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
    

    

def generate_single_meal(calories_per_meal:int, food_options:list[Food]):
    meal = {}
    protein_choice = choose_random_macro(Food_type.PROTEIN, food_options)
    carb_choice = choose_random_macro(Food_type.CARB, food_options)
    fat_choice = choose_random_macro(Food_type.FAT, food_options)
    micro_choice = choose_random_macro(Food_type.MICRONUTRIENT, food_options)

    protein_per_meal = calories_per_meal * 0.33
    carbs_per_meal = calories_per_meal * 0.33
    fat_per_meal = calories_per_meal * 0.10
    total_macros = protein_per_meal + carbs_per_meal + fat_per_meal
    micros_per_meal = calories_per_meal - total_macros

    protein_servings = meet_requirement(protein_choice, protein_per_meal)
    carb_servings = meet_requirement(carb_choice, carbs_per_meal)
    fat_servings = meet_requirement(fat_choice, fat_per_meal)
    micro_servings = meet_requirement(micro_choice, micros_per_meal)

    p_cal, p_pro, p_carb, p_fat = generate_nutrition_facts(protein_choice, protein_servings)
    c_cal, c_pro, c_carb, c_fat = generate_nutrition_facts(carb_choice, carb_servings)
    f_cal, f_pro, f_carb, f_fat = generate_nutrition_facts(fat_choice, fat_servings)
    m_cal, m_pro, m_carb, m_fat = generate_nutrition_facts(micro_choice, micro_servings)

    total_calories = p_cal + c_cal + f_cal + m_cal
    total_protein = p_pro + c_pro + f_pro + m_pro
    total_carbs = p_carb + c_carb + f_carb + m_carb
    total_fat = p_fat + c_fat + f_fat + m_fat
    return total_calories, total_protein, total_carbs, total_fat




    



    


def meet_requirement(food:Food, allowance:int)->int:
    servings = round(allowance/food.calories, 2)
    print(f"You can have {round(servings,2)} servings of {food.name} for {round(food.calories * servings, 2)} calories")
    return servings


def choose_random_macro(macro_type:Food_type, foods:list[Food])->Food:
    matching_foods = [food for food in foods if getattr(food, "food_type", None)== macro_type]
    if not matching_foods:
        raise ValueError(f"No food items found of {macro_type}") 
    choice = random.choice(matching_foods)
    print(f"The chosen food is {choice.name} because it is a {choice.food_type}")
    return choice
    
    
def generate_nutrition_facts(food:Food, servings:int)->int:
    total_calories = food.calories * servings
    total_protein = food.protein * servings
    total_carbs = food.carbs * servings
    total_fat = food.fat * servings
    print(f"{food.name} - {servings} servings - {round(food.serving_size * servings,2)} grams - {round(total_calories,2)} total calories, {round(total_protein, 2)} grams protein, {round(total_carbs,2)} grams carbs, {round(total_fat, 2)} grams fat")
    return total_calories, total_protein, total_carbs, total_fat
 
    
