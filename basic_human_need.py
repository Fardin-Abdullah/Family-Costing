class Basic_Human_Need :
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    class Food:
        class nutritions_calculator:
        
            def __init__(self,name,age,gender,height,weight,af,cf):
                self.name = name
                self.age = age
                self.gender = gender
                self.height = height
                self.weight = weight
                self.activity_factor = af
                self.climate_factor = cf 
            
            def BMR(self):
                
                if self.gender.lower() == "male":

                    bmr = (10 * self.weight) + (6.25 * self.height) - (5 * self.age) + 5
                
                elif self.gender.lower() == "female":

                    bmr = (10 * self.weight) + (6.25 * self.height) - (5 * self.age) - 161

                else:

                    print("Please enter your correct gender")

                return bmr
            
            def BMI(self):

                BMI = self.weight / (self.height/100) ** 2
                return  BMI
            
            def check_BMI(self):

                if self.BMI() < 18.5 :

                    print("Your BMI is ",self.BMI(),"\nUnderweight \n21.7 is perfect BMI \nYou have to gain weight")
                    self.gain_perfect_weight()

                elif 18.5 <= self.BMI() < 21.7 or 21.7 <= self.BMI() < 24.9 :

                    print("Healthy Weight")
                    if self.BMI() == 21.7 :
                        print("Perfect Weight")

                elif 25 < self.BMI() < 29.9 :

                    print("YOur BMI is",self.BMI(),"Overweight \n21.7 is perfect BMI")
                    self.gain_perfect_weight()

                else :

                    print("Obese \n21.7 is perfect BMI")
                    self.gain_perfect_weight()

            def calc_daily_cal(self):

                dcn = self.BMR() * self.activity_factor
                return dcn
            


            def calc_protein(self):

                protein = self.calc_daily_cal() / 20
                return protein
            
            def calc_carb(self):

                carb = (55 * self.calc_daily_cal()) / 400
                return carb 
            
            def calc_fat(self):

                fat = (27.5 * self.calc_daily_cal()) / 900
                return fat
            
            def calc_df(self):

                df = (self.calc_daily_cal() / 1000) * 14
                return df 

            def calc_water(self):

                #water = 0.0296 * self.weight
                water = (self.weight * self.activity_factor * self.climate_factor) / 28.4
                return water 
            


            def gain_perfect_weight(self):

                target_weight = 21.7 * (((self.height) / 100)** 2)
                self.weight = target_weight
                gender_prefix = {"male": "Sir", "female": "Ms"}

                if self.gender.lower() in gender_prefix:
                    prefix = gender_prefix[self.gender.lower()]
                    info_lines = [
                        f"{prefix} you have to maintain BMI {self.BMI()}",
                        f"{prefix} your need to maintain BMR {self.BMR()}",
                        f"{prefix} you need {self.calc_daily_cal()} kcal per day",
                        f"{prefix} you need {self.calc_protein()} gm of protein per day",
                        f"{prefix} you need {self.calc_carb()} gm of carbs per day",
                        f"{prefix} you need {self.calc_fat()} gm of fat per day",
                        f"{prefix} you need {self.calc_df()} gm of dietary fiber per day",
                        f"{prefix} you need {self.calc_water()} L of water per day"
                    ]
                    print("\n".join(info_lines))
                else:
                    print("Please enter your correct gender") 
                
            def printInfo(self):

                if  18.5 < self.BMI() < 24.9 :

                    gender_prefix = {"male": "Sir", "female": "Ms"}

                    if self.gender.lower() in gender_prefix:
                        prefix = gender_prefix[self.gender.lower()]
                        info_lines = [
                            f"{prefix} your BMI is {self.BMI()}",
                            f"{prefix} your BMR is {self.BMR()}",
                            f"{prefix} you need {self.calc_daily_cal()} gm of calories per day",
                            f"{prefix} you need {self.calc_protein()} gm of protein per day",
                            f"{prefix} you need {self.calc_carb()} gm of carbs per day",
                            f"{prefix} you need {self.calc_fat()} gm of fat per day",
                            f"{prefix} you need {self.calc_df()} gm of dietary fiber per day",
                            f"{prefix} you need {self.calc_water()} L of water per day"
                        ]
                        print("\n".join(info_lines))
                    else:
                        print("Please enter your correct gender")
                
                else:
                    self.check_BMI()



        

        def get_user_height():

                unit_choice = input("Enter preferred height unit (cm/feet): ").lower()

                if unit_choice == "cm":

                    return float(input("Enter height in centimeters: "))
                
                elif unit_choice == "feet":
                    
                    feet = int(input("Enter feet: "))
                    inches = int(input("Enter inches: "))
                    total_height_cm = (feet * 30.48) + (inches * 2.54)  # Convert feet and inches to centimeters
                    return total_height_cm

                else:

                    print("Invalid choice. Please enter 'cm' or 'feet'.")
                    # return Basic_Human_Need.Food.nutritions_calculator.get_user_height()

        def get_user_weight():

                unit_choice = input("Enter preferred weight unit (kg/lbs): ").lower()

                if unit_choice == "kg":

                    return float(input("Enter weight in kilograms: "))
                
                elif unit_choice == "lbs":

                    lbs = float(input("Enter weight in pounds: "))
                    return lbs * 0.4536  # Convert pounds to kilograms
                
                else:
                    
                    print("Invalid choice. Please enter 'kg' or 'lbs'.")
                    #return get_user_weight()


            
        def activity_level():
                al = {
                    "sedentary-->Little to no exercise": 1.2,
                    "lightly_active-->Light exercise (1-3 days per week)": 1.375,
                    "moderate-->Moderate exercise (3-5 days per week)": 1.55,
                    "very_active-->Heavy exercise (6-7 days per week)": 1.725,
                    "extra_active-->Very heavy exercise (twice per day, extra physical job)": 1.9
                }

                print("Choose an activity level:")

                for index, option in enumerate(al.keys(), start=1):

                    print(f"{index}. {option}")

                try:

                    choice = int(input("Enter the number corresponding to your choice: "))
                    selected_level = list(al.keys())[choice - 1]
                    print(f"Selected activity level: {selected_level} ({al[selected_level]})")
                    activity_factor = al[selected_level]
                    
                    return activity_factor
                
                except (ValueError, IndexError):

                    print("Invalid choice. Please enter a valid number.")
        def climate_factor():

                cf = {"Hot and Humid climate":1.2,
                    "Moderate Climate":1.2,
                    "Cold and dry Climate":0.8}
                
                print("Choose an activity level:")

                for index, option in enumerate(cf.keys(), start=1):

                    print(f"{index}. {option}")

                try:

                    choice = int(input("Enter the number corresponding to your choice: "))
                    selected_level = list(cf.keys())[choice - 1]
                    print(f"Selected climate factor: {selected_level} ({cf[selected_level]})")
                    climate_factor = cf[selected_level]
                    
                    return climate_factor
                
                except (ValueError, IndexError):
                    
                    print("Invalid choice. Please enter a valid number.")

    class ClothingStore:
    
        def __init__(self,item_name,price,quantity):
            self.item = item_name
            self.price = price
            self.quantity = quantity
            # Initialize an empty dictionary to store items
            self.items = {}

        def add_item(self, item_name, price, quantity):
            """
            Add an item to the store with its price and quantity.
            Args:
                item_name (str): Name of the clothing item.
                price (float): Price of the item.
                quantity (int): Quantity of the item.
            """
            self.items[item_name] = {"price": price, "quantity": quantity}

        def add_item(self, item_name, price, quantity):
            """
            Add an item to the store with its price and quantity.
            Args:
                item_name (str): Name of the clothing item.
                price (float): Price of the item.
                quantity (int): Quantity of the item.
            """
            self.items[item_name] = {"price": price, "quantity": quantity}

        def calculate_total_price(self):
            """
            Calculate the total price of all items in the store.
            Returns:
                float: Total price.
            """
            total_price = sum(item["price"] * item["quantity"] for item in self.items.values())
            return total_price

 
    class TreatmentCostCalculator:
        def __init__(self):
            self.treatment_prices = {}  # Dictionary to store treatment names and their prices

        def add_treatment(self, treatment_name, price):
            self.treatment_prices[treatment_name] = price

        def calculate_total_cost(self, selected_treatments):
            total_cost = sum(self.treatment_prices.get(treatment, 0) for treatment in selected_treatments)
            return total_cost

                    
    class EducationCostTracker:
        def __init__(self):
            self.costs = {}  # Dictionary to store education costs

        def add_cost(self, education_type, cost):
            """
            Add education cost for a specific type (school, college, varsity, or PhD).
            Args:
                education_type (str): Type of education (e.g., 'school', 'college', 'varsity', 'PhD')
                cost (float): Cost for the education type
            """
            self.costs[education_type.lower()] = cost

        def get_total_cost(self):
            """
            Calculate the total education cost.
            Returns:
                float: Total cost
            """
            return sum(self.costs.values())

class Cost_Per_person:
    def __init__(self,person):
        self.person = person

    def cloth_cost(self,person):
        return self.person.ClothingStore.add_item(),person.ClothingStore.calculate_total_price()
    def treatment_cost(self,person):
        self.person.TreatmentCostCalculator.add_treatment()
        self.person.TreatmentCostCalculator.calculate_total_cost()
    def education_Cost(self,person):
        self.person.EducationCostTracker.add_cost()
        self.person.EducationCostTracker.get_total_cost()
    def foodCost(self,person):

        self.person.Food.nutritions_calculator()
        name = input("Enter your name :")
        age = int(input("Enter your age:"))
        gender = input("Entter your gender:")
        height = Basic_Human_Need.Food.get_user_height()
        weight= Basic_Human_Need.Food.get_user_weight()
        al= Basic_Human_Need.Food.activity_level()
        af= Basic_Human_Need.Food.nutritions_calculator.activity_factor()
        cf= Basic_Human_Need.Food.climate_factor()
        obj = Basic_Human_Need.Food.nutritions_calculator(name,age,gender,height,weight,af,cf)
        obj.printInfo()

    def total_cost_of_everything(self,person):
        total_Cost = self.person.ClothingStore.calculate_total_price() + self.person.EducationCostTracker.get_total_cost()
        return total_Cost
def main():
    members = int(input("How many members do you have in your family?"))
    i = 1
    while members >= i :
        print("Member",i)
        person = input("Enter your name :")
        age = int(input("Enter your age:"))
        gender = input("Entter your gender:")
        person = Basic_Human_Need(person,age,gender)
        f = Cost_Per_person(person)
        print(f)
        i+=1

if __name__ == "__main__":

    main()







