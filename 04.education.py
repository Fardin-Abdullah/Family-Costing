class EducationCostTracker:
    def __init__(self):
        self.costs = {}

    def add_cost(self, education_type, cost):
        """
        Add education cost for a specific type (school, college, varsity, or PhD).
        Args:
            education_type (str): Type of education (e.g., 'school', 'college').
            cost (float): Cost for the education type.
        """
        self.costs[education_type.lower()] = cost

    def get_total_cost(self):
        """
        Calculate the total education cost.
        Returns:
            float: Total cost.
        """
        return sum(self.costs.values())

# Example usage:
tracker = EducationCostTracker()

# Get user input for different education types
while True:
    education_type = input("Enter education type (school/college/varsity/PhD or 'done' to finish): ")
    if education_type.lower() == 'done':
        break
    cost = float(input(f"Enter cost for {education_type}: "))
    tracker.add_cost(education_type, cost)

# Get the total cost
total_cost = tracker.get_total_cost()
print(f"Total education cost: ${total_cost:.2f}")
