class ClothingStore:
    def __init__(self):
        self.items = {}  # Dictionary to store item names, prices, and quantities

    def add_item(self, item_name, price, quantity):
        self.item = item_name
        self.price = price
        self.quantity = quantity
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

# Example usage:
store = ClothingStore()
store.add_item("Shirt", price=25.99, quantity=2)
store.add_item("Jeans", price=39.99, quantity=1)
store.add_item("Socks", price=5.99, quantity=5)

total_price = store.calculate_total_price()
print(f"Total price for clothing: ${total_price:.2f}")
