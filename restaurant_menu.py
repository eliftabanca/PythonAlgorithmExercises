#Write a Python class that stores the names, prices, and popularity ratings of dishes in a restaurant's menu. 
#The class should use list data structures to store the dish names, prices, and popularity ratings respectively. 
#Use sample data for the dishes, prices, and popularity ratings. Then, create an instance of this class andprint these values.

class ShoppingCart:
    def __init__(self):
        self.shopping = [
            ["Bag", "50", "10"],
            ["Pants", "400", "4"],
            ["T-shirt", "100", "2"]
        ]

    def display_cart(self):
        for item in self.shopping:
            print(f"Cart: {item[0]}, Price: {item[1]}, Quantity: {item[2]}")

# Example usage
cart = ShoppingCart()
cart.display_cart()