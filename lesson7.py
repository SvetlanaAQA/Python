def requestUserInput(message):
    value = input(message)
    while not value:
        value = input(message)
    return value
    

def requestUserInputFloat (message):
    while True:
        value = requestUserInput(message)
        try:
            return float(value)
        except ValueError:
            print ("You need input number")
 
class Product(): 
    def __init__(self ):

        self.productName = requestUserInput("Enter name:")
        self.weight = requestUserInputFloat ("Enter weight (g): ")
        self.protein = requestUserInputFloat("Enter protein per 100g: ")
        self.fat = requestUserInputFloat("Enter fat per 100g: ")
        self.carbs = requestUserInputFloat("Enter carbs per 100g: ")
        self.totalProtein  = self.weight * self.protein / 100
        self.totalFat = self.weight * self.fat / 100
        self.totalCarbs = self.weight * self.carbs / 100
        self.totalEnergy = self.totalProtein * 4 + self.totalFat * 9 + self.totalCarbs * 4
        print(self.productName  +" Energy: " + str(self.totalEnergy) + "Kkal")
        print("Protein: " + str(self.totalProtein) + "g")
        print("Fat: "+ str(self.totalFat) + "g")
        print("Carbs: "+ str(self.totalCarbs) + "g")
emp2 = Product()