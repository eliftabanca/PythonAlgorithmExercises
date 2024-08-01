#Write an algorithm that keeps the daily sales amount, product name, and price of a store
#as a list and calculates the total sales revenue.

products = ["Phone", "Computer", "Tablet"]
quantities = [6, 10, 11]
prices = [200, 400, 300]

total_income = 0

for i in range(len(products)):
    total_income = (quantities[i] * prices[i]) + total_income
    print(f"Product name: {products[i]}, Product quantity:: {quantities[i]}, Product price: {prices[i]}")
print(f"Total income: {total_income} ")



 