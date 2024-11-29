class SafetyCostTracker:
    def __init__(self):
        self.safety_measures = {}

    def add_cost(self, measure, cost):
        """
        Add cost for a specific safety measure (e.g., insurance, security systems).
        Args:
            measure (str): Type of safety measure.
            cost (float): Cost for the measure.
        """
        self.safety_measures[measure.lower()] = cost

    def get_total_cost(self):
        """
        Calculate the total safety-related cost.
        Returns:
            float: Total cost for safety measures.
        """
        return sum(self.safety_measures.values())

# Example usage:
tracker = SafetyCostTracker()

# Prompt user to add safety measures
while True:
    measure = input("Enter safety measure (e.g., insurance, security) or 'done' to finish: ")
    if measure.lower() == 'done':
        break
    cost = float(input(f"Enter cost for {measure}: "))
    tracker.add_cost(measure, cost)

# Calculate and display total cost
total_cost = tracker.get_total_cost()
print(f"The total cost for safety measures is ${total_cost:.2f}")
