numbers = [int(x) for x in input("Enter list elements: ").split()]
value = int(input("Enter element to remove: "))
if value in numbers:
    numbers.remove(value)
else:
    print("Element not found")
print(numbers)
