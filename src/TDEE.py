
def generate_TDEE(weight:int, height:int, age:int, gender:str, activity_level: int)->int:
    if gender == "male":
        BMR = (10*weight) +(6.25*height)-(5*age)+5
    else:
        BMR = (10*weight) +(6.25*height)-(5*age)-161
    match activity_level:
        case 1:
            activity_factor = 1.2
        case 2:
            activity_factor = 1.375
        case 3:
            activity_factor = 1.55
        case 4:
            activity_factor = 1.725
        case 5:
            activity_factor = 1.9
    TDEE = BMR * activity_factor
    print("Your TDEE is ", TDEE)
    return TDEE

def generate_TDEE_imperial(weight:int, height:int, age:int, gender:str, activity_level: int)->int:
    if gender == "male":
        BMR = (6.25*weight) +(12.7*height)-(6.75*age)+ 66
    else:
        BMR = (6.25*weight) +(12.7*height)-(6.75*age)-161
    match activity_level:
        case 1:
            activity_factor = 1.2
        case 2:
            activity_factor = 1.375
        case 3:
            activity_factor = 1.55
        case 4:
            activity_factor = 1.725
        case 5:
            activity_factor = 1.9
    TDEE = BMR * activity_factor
    print("Your TDEE is ", TDEE)
    return TDEE

    