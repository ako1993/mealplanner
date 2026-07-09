from utils import generate_menu, get_user_info, generate_user_prompt
from TDEE import generate_TDEE
import sys

print("Welcome to the meal planner!")
generate_menu()
user_selection = int(input())
if user_selection == 1:
    weight, height, age, gender, activity_level = get_user_info()
    user_TDEE = generate_TDEE(weight, height, age, gender, activity_level)
    user_choice = generate_user_prompt(user_TDEE)
    if user_choice == 1:
        print("Generating meal plan....")
    else:
        sys.exit(0)
        

