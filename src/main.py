from utils import generate_menu, get_user_info, generate_user_prompt, finalize_plan, menu_for_no_TDEE, generate_ascii_art
from TDEE import generate_TDEE
from meal_generator import generate_meals
import sys

generate_ascii_art()
generate_menu()
user_selection = int(input())
if user_selection == 1:
    weight, height, age, gender, activity_level = get_user_info()
    user_TDEE = generate_TDEE(weight, height, age, gender, activity_level)
    user_choice = generate_user_prompt(user_TDEE)
    if user_choice == 1:
        generate_meals(user_TDEE)
        finalize_plan(user_TDEE)
    else:
        sys.exit(0)
elif user_selection == 2:
    menu_for_no_TDEE()
    
        

