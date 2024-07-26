#A perfect number is a positive integer that is equal to the sum of its proper divisors, excluding itself.
#Write a Python program to determine whether a number is a perfect number.


number = int(input("Enter a number: "))
def perfect_number(number):
    total = 0

    for i in range(1, number):
        if number % i == 0:
            total += i

    if total == number:
        return "The number is a perfect number."
    else:
        return "The number is not a perfect number."


print(perfect_number(number))