from food import Food
from clothing import ClothingStore
from treatment import TreatmentCostCalculator
from shelter import ShelterCostCalculator
from education import EducationCostTracker
from safety import SafetyCostTracker

def main():
    print("Welcome to the Family Expense Tracker!")

    # Food
    print("\n--- Food Section ---")
    Food.main()  # Assuming you use `main()` as the entry point in `food.py`.

    # Clothing
    print("\n--- Clothing Section ---")
    clothing_store = ClothingStore()
    clothing_store.add_item("Shirt", 25.99, 2)
    clothing_store.add_item("Jeans", 39.99, 1)
    total_clothing_cost = clothing_store.calculate_total_price()
    print(f"Total clothing cost: ${total_clothing_cost:.2f}")

    # Treatment
    print("\n--- Treatment Section ---")
    treatment_calculator = TreatmentCostCalculator()
    treatment_calculator.add_treatment("Dental Checkup", 100.0)
    total_treatment_cost = treatment_calculator.calculate_total_cost(["Dental Checkup"])
    print(f"Total treatment cost: ${total_treatment_cost:.2f}")

    # Shelter
    print("\n--- Shelter Section ---")
    shelter_calculator = ShelterCostCalculator()
    shelter_calculator.add_shelter_cost("Rent", 1200.0)
    shelter_calculator.add_shelter_cost("Utilities", 200.0)
    total_shelter_cost = shelter_calculator.get_total_cost()
    print(f"Total shelter cost: ${total_shelter_cost:.2f}")

    # Education
    print("\n--- Education Section ---")
    education_tracker = EducationCostTracker()
    education_tracker.add_cost("School", 300.0)
    total_education_cost = education_tracker.get_total_cost()
    print(f"Total education cost: ${total_education_cost:.2f}")

    # Safety
    print("\n--- Safety Section ---")
    safety_tracker = SafetyCostTracker()
    safety_tracker.add_cost("Insurance", 500.0)
    total_safety_cost = safety_tracker.get_total_cost()
    print(f"Total safety cost: ${total_safety_cost:.2f}")

    print("\nExpense tracking completed!")

if __name__ == "__main__":
    main()
