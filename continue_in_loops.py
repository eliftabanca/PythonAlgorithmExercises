numbers = [2, 4, -1, 7, -13, 20, -3, 66]
positives = []

for number in numbers:
    if number < 0:
        continue 
    positives.append(number)  

print(f"Positive numbers: {positives}")
