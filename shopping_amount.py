total_price = 0

product_number = int(input("How many products would you like to buy? "))

for i in range(1, product_number + 1):
    product_price = float(input(f"Price of product {i}: "))
    total_price += product_price

print(f"Total shopping amount: {total_price}")
