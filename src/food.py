from enum import enum, auto

class Food_type(enum):
        PROTEIN = auto()
        FAT = auto()
        CARB = auto()
        MICRONUTRIENT = auto()

class Food():
    def __init__(self, serving_size:int, calories:int, protein:int, carbs:int, fat:float, food_type:Food_type):
        self.serving_size = serving_size
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat
        self.food_type = food_type

    def getChicken()->Food:
        chicken = Food(114, 110, 23, 0, 2.5, Food_type.Protein)
        return chicken
    
    def getBrownRice()->Food:
         brown_rice = Food(45, 170, 3, 34, 1.5, Food_type.CARB)
         return brown_rice

    def getAvacado()->Food:
         avacado = Food(50, 80, 1, 4, 7, Food_type.FAT)
         return avacado
    
    def getBrocolli()->Food:
         brocolli = Food(85, 30, 2, 6, 0, Food_type.MICRONUTRIENT)
         return brocolli

