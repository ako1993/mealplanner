from utils import generate_menu, get_user_info
from TDEE import generate_TDEE

print("Welcome to the meal planner!")
generate_menu()
user_selection = int(input())
if user_selection == 1:
    weight, height, age, gender, activity_level = get_user_info()
    generate_TDEE(weight, height, age, gender, activity_level)

