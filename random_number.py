import random

def guess_number():
    random_num = random.randint(1, 10)
    while True:
        number = int(input("Enter a number between 1 and 10: "))
        if number == random_num:
            print(f"The target number is {random_num}, which matches your guess of {number}.")
            break
        elif number > random_num:
            print("Try a lower number...")
        else:
            print("Try a higher number...")

guess_number()

