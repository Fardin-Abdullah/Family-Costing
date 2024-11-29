import basic_human_need as bsn
class FinalCost:
    def __init__(self,name=None,age=None,gender=None):
        self.name = name
        self.age = age
        self.gender = gender
    
    def total_food_cost():
        pass

    def total_cloth_cost(self):
    
        n = int(input("How many different items do you want?"))
        total_cloth_cost = 0
        for _ in range(n):
            item_name = input("Please enter your item name: ")
            price = float(input("Please enter the price of your item: "))
            quantity = int(input("Please enter the quantity: "))
            cloth_object = bsn.Basic_Human_Need.ClothingStore(item_name, price, quantity)
            cloth_object.add_item(item_name,price,quantity)
            total_cloth_cost = total_cloth_cost + cloth_object.calculate_total_price()
        print(f"Total clothing cost: ${total_cloth_cost:.2f}")
        return total_cloth_cost
    
    def total_sheltering_cost():
        pass


    def total_treatment_cost(self):
        
            total_treatment_cost = 0
            n = int(input("How many different treatments do you want?"))
            for _ in range(n):
                treatment_name = input("Please enter your treatment name: ")
                price = float(input("Enter the price for treatment: "))
                treatment_object = bsn.Basic_Human_Need.TreatmentCostCalculator()
                treatment_object.add_treatment(treatment_name, price)
                total_treatment_cost = total_treatment_cost + treatment_object.calculate_total_cost()
            return total_treatment_cost
    
    def total_education_cost():
        pass

    def total_safety_cost():
        pass

    def total_cost_of_allNeed():
        pass

def select_need():
    bsno = {
        "Food": 1,
        "Clothing": 2,
        "Shelter": 3,
        "Treatment": 4,
        "Education": 5,
        "Safety": 6,
        "All": 7
    }

    print("Choose an option")

    for index, (option, _) in enumerate(bsno.items(), start=1):
        print(f"{index}. {option}")

    try:
        choice = int(input("Enter the number corresponding to your choice: "))
        selected_need = list(bsno.keys())[choice - 1]
        return selected_need
    except (ValueError, IndexError):
        print("Invalid choice. Please enter a valid number.")

def main():
    members = int(input("How many members do you have in your family?"))
    i = 1
    while members >= i :
        print("Member",i)
        name = input("Enter your name :")
        age = int(input("Enter your age:"))
        gender = input("Entter your gender:")
        i += 1
    
    sn = select_need()
    print(sn)
    p = FinalCost(name,age,gender)
    if sn == "Food":
        pass
    elif sn == "Clothing":
      p.total_cloth_cost()
    elif sn == "Shelter":
        pass
    elif sn == "Treatment":
        print("Your total cost for treatment is", p.total_treatment_cost())
    elif sn == "Education":
        pass
    elif sn == "Safety":
        pass
    else:
        pass

if __name__ == "__main__":
    main()