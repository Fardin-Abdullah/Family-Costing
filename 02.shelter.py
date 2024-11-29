class ShelterCostCalculator:
    def __init__(self):
        self.shelter_costs = {}

    def add_shelter_cost(self, shelter_type, cost):
        """
        Add shelter cost for a specific type (rent, utilities, maintenance, etc.).
        Args:
            shelter_type (str): Type of shelter cost (e.g., 'rent', 'utilities').
            cost (float): Cost amount for the shelter type.
        """
        self.shelter_costs[shelter_type.lower()] = cost

    def get_total_cost(self):
        """
        Calculate the total shelter cost.
        Returns:
            float: Total cost of shelter.
        """
        return sum(self.shelter_costs.values())

# Example usage:
calculator = ShelterCostCalculator()

# Prompt user to add shelter costs
while True:
    shelter_type = input("Enter shelter cost type (e.g., rent, utilities) or 'done' to finish: ")
    if shelter_type.lower() == 'done':
        break
    cost = float(input(f"Enter cost for {shelter_type}: "))
    calculator.add_shelter_cost(shelter_type, cost)

# Calculate and display total shelter cost
total_cost = calculator.get_total_cost()
print(f"The total cost for shelter is ${total_cost:.2f}")
