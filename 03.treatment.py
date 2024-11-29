class TreatmentCostCalculator:
    def __init__(self):
        self.treatment_prices = {}  # Dictionary to store treatment names and their prices

    def add_treatment(self,treatment_name, price):
        self.treatment_prices[treatment_name] = price

    def calculate_total_cost(self, selected_treatments):
        total_cost = sum(self.treatment_prices.get(treatment, 0) for treatment in selected_treatments)
        return total_cost

# Example usage:
calculator = TreatmentCostCalculator()

# Prompt user to add treatments and their prices
while True:
    treatment_name = input("Enter treatment name (or 'done' to finish): ")
    if treatment_name.lower() == 'done':
        break
    price = float(input(f"Enter price for {treatment_name}: "))
    calculator.add_treatment(treatment_name, price)

# Prompt user to select treatments (you can customize this part)
selected_treatments = []
while True:
    treatment_choice = input("Select a treatment (or 'done' to calculate total cost): ")
    if treatment_choice.lower() == 'done':
        break
    selected_treatments.append(treatment_choice)

total_cost = calculator.calculate_total_cost(selected_treatments)

print(f"The total cost for the selected treatments is ${total_cost:.2f}")
