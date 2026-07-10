from enum import Enum, auto

class Food_type(Enum):
        PROTEIN = auto()
        FAT = auto()
        CARB = auto()
        MICRONUTRIENT = auto()

class Food():
    def __init__(self, name:str, serving_size:int, calories:int, protein:int, carbs:int, fat:float, food_type:Food_type):
        self.name = name
        self.serving_size = serving_size
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat
        self.food_type = food_type

    def getChicken():
        chicken = Food("chicken", 114, 110, 23, 0, 2.5, Food_type.PROTEIN)
        return chicken
    
    def getBrownRice():
         brown_rice = Food("brown rice", 45, 170, 3, 34, 1.5, Food_type.CARB)
         return brown_rice

    def getAvacado():
         avacado = Food("avacado", 50, 80, 1, 4, 7, Food_type.FAT)
         return avacado
    
    def getBrocolli():
         brocolli = Food("brocolli", 85, 30, 2, 6, 0, Food_type.MICRONUTRIENT)
         return brocolli
    
    def getBeef():
         beef = Food("beef", 114, 170, 23, 0, 8, Food_type.PROTEIN)
         return beef
    
    def getSweetPotato():
         sweet_potato = Food("sweet potato", 110, 110, 2, 24, 0, Food_type.CARB)
         return sweet_potato
    
    def getPeanutButter():
         peanut_butter = Food("peanut butter", 32, 190, 8, 7, 16, Food_type.FAT)
         return peanut_butter
    
    def getAsparagus():
         asparagus = Food("asparagus", 84, 15, 2, 3, 0, Food_type.MICRONUTRIENT)
         return asparagus

