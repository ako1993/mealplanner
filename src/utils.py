from meal_generator import generate_meals


def generate_menu():
    print('''Please select one of the following options:
          
To calculate your daily TDEE press 1 and enter
To generate a custom meal plan based on your daily calories
press 2 and enter
            ''')
    
def generate_user_prompt(user_TDEE:float)->int:
    while True:
        print("Do you want to generate a meal plan based on your TDEE of ", user_TDEE, "?")
        user_selection = int(input("Select 1 to generate plan and 2 to exit the program "))
        if user_selection == 1 or user_selection == 2:
            break
        else:
            print("Please select 1 or 2")
    return user_selection

def get_user_info():
    while True:
        try:
            user_weight = float(input("What is your weight in KG? "))
            if user_weight < 1:
                print("Please enter a valid weight")
            else:
                break
        except ValueError as v:
            print(f"Input error! {v}")
    while True:
        try:
            user_height = float(input("What is your height in CM? "))
            if user_height < 1:
                print("Please enter a valid height")
            else:
                break
        except ValueError as v:
            print(f"Input error! {v}")
    while True:
         try:
            user_age = int(input("What is your age? "))
            if user_age < 1:
                print("Please enter a valid age")
            else:
                break
         except ValueError as v:
            print(f"Input error! {v}")
    while True:
        user_gender = input("What is your gender? ")
        if user_gender == 'male' or user_gender == 'female':
            break
        else:
            print("Please enter a valid gender")
    while True:
        try:
            activity_level = int(input("What is your activity level on a scale from 1 to 5? "))
            if activity_level < 1 or activity_level > 5:
                print("please select a value between 1 and 5")
            else:
                break
        except ValueError as v:
            print(f"Input error! {v}")
    return user_weight, user_height, user_age, user_gender, activity_level
    
def finalize_plan(TDEE:float):
    user_selection = input("To finalize select 1\nto generate a new plan to gain weight select 2\nto generate a new plan to lose weight select 3\nto generate a new plan based on your TDEE select 4\n")
    match user_selection:
        case "1":
            return
        case "2":
            TDEE = TDEE + TDEE * 0.1
            generate_meals(TDEE)
            finalize_plan(TDEE)
        case "3":
            TDEE = TDEE - TDEE * 0.1
            generate_meals(TDEE)
            finalize_plan(TDEE)
        case "4":
            generate_meals(TDEE)
            finalize_plan(TDEE)
        case _:
            print("Please select a valid option")
            finalize_plan(TDEE)

def menu_for_no_TDEE():
    user_selection = int(input("How many calories would you like to consume? "))
    generate_meals(user_selection)
    finalize_plan(user_selection)

def generate_ascii_art():
    print(r"""
    __  ___           __   ______                           __            
   /  |/  /__  ____ _/ /  / ____/__  ____  ___  _________ _/ /_____  _____
  / /|_/ / _ \/ __ `/ /  / / __/ _ \/ __ \/ _ \/ ___/ __ `/ __/ __ \/ ___/
 / /  / /  __/ /_/ / /  / /_/ /  __/ / / /  __/ /  / /_/ / /_/ /_/ / /    
/_/  /_/\___/\__,_/_/   \____/\___/_/ /_/\___/_/   \__,_/\__/\____/_/     
""")