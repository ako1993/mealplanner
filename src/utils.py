def generate_menu():
    print('''Please select one of the following options:
          
To calculate your daily TDEE press 1 and enter
To generate a custom meal plan based on your daily calories
press 2 and enter
            ''')
    
def get_user_info():
    while True:
        user_weight = float(input("What is your weight in KG?"))
        if user_weight < 1:
            print("Please enter a valid weight")
        else:
            break
    while True:
        user_height = float(input("What is your height in CM?"))
        if user_height < 1:
            print("Please enter a valid height")
        else:
            break
    while True:
        user_age = int(input("What is your age?"))
        if user_age < 1:
            print("Please enter a valid age")
        else:
            break
    while True:
        user_gender = input("What is your gender?")
        if user_gender == 'male' or user_gender == 'female':
            break
        else:
            print("Please enter a valid gender")
    while True:
        activity_level = int(input("What is your activity level on a scale from 1 to 5?"))
        if activity_level < 1 or activity_level > 5:
            print("please select a value between 1 and 5")
        else:
            break
    return user_weight, user_height, user_age, user_gender, activity_level
    