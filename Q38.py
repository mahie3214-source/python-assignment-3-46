numbers = [int(x) for x in input("Enter numbers: ").split()]
unique = []
for number in numbers:
    if number not in unique:
        unique.append(number)
print("Without duplicates:", unique)
