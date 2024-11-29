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
        
        def onlyprintInfo(self):
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



def main():

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
            return get_user_height()

    def get_user_weight():

        unit_choice = input("Enter preferred weight unit (kg/lbs): ").lower()

        if unit_choice == "kg":

            return float(input("Enter weight in kilograms: "))
            
        elif unit_choice == "lbs":

            lbs = float(input("Enter weight in pounds: "))
            return lbs * 0.4536  # Convert pounds to kilograms
            
        else:
                
            print("Invalid choice. Please enter 'kg' or 'lbs'.")
            return get_user_weight()


        
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

       
    members = int(input("How many members do you have in your family?"))
    i = 1
    while members >= i :
        print("Member",i)
        name = input("Enter your name :")
        age = int(input("Enter your age:"))
        gender = input("Entter your gender:")
        height = get_user_height()
        weight = get_user_weight()
        af = activity_level()
        cf = climate_factor()
        obj = Food()
        obj = obj.nutritions_calculator(name,age,gender,height,weight,af,cf)
        obj.onlyprintInfo()
        i += 1 
        obj.gain_perfect_weight()

if __name__ == "__main__":
    main()
