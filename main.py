from utils import generate_menu

print("Welcome to the meal planner!")
generate_menu()
user_selection = int(input())
if user_selection == 1:
    print("Generating TDEE")

