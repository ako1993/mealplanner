def generate_menu():
    print('''Please select one of the following options:
          
To calculate your daily TDEE press 1 and enter
To generate a custom meal plan based on your daily calories
press 2 and enter
            ''')
    
def generate_user_prompt(user_TDEE:float)->int:
    while True:
        print("Do you want to generate a meal plan based on your TDEE of ", user_TDEE, "?")
        user_selection = int(input("Select 1 to generate plan and 2 to exit the program"))
        if user_selection == 1 or user_selection == 2:
            break
        else:
            print("Please select 1 or 2")
    return user_selection

def get_user_info():
    while True:
        try:
            user_weight = float(input("What is your weight in KG?"))
            if user_weight < 1:
                print("Please enter a valid weight")
            else:
                break
        except ValueError as v:
            print(f"Input error! {v}")
    while True:
        try:
            user_height = float(input("What is your height in CM?"))
            if user_height < 1:
                print("Please enter a valid height")
            else:
                break
        except ValueError as v:
            print(f"Input error! {v}")
    while True:
         try:
            user_age = int(input("What is your age?"))
            if user_age < 1:
                print("Please enter a valid age")
            else:
                break
         except ValueError as v:
            print(f"Input error! {v}")
    while True:
        user_gender = input("What is your gender?")
        if user_gender == 'male' or user_gender == 'female':
            break
        else:
            print("Please enter a valid gender")
    while True:
        try:
            activity_level = int(input("What is your activity level on a scale from 1 to 5?"))
            if activity_level < 1 or activity_level > 5:
                print("please select a value between 1 and 5")
            else:
                break
        except ValueError as v:
            print(f"Input error! {v}")
    return user_weight, user_height, user_age, user_gender, activity_level
    