class Product:
    shop_name = "MegaShop"

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def sell(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity
            print(f"Sold {quantity} {self.name}, remaining: {self.stock}")
        else:
            print(f"Not enough {self.name} in stock!")


# Create a product object
product1 = Product("laptops", 800, 10)

# Display initial stock
print("Shop:", product1.shop_name)
print("Initial stock:", product1.stock)

# Sell 2 laptops
product1.sell(2)

# Display updated stock
print("Updated stock:", product1.stock)