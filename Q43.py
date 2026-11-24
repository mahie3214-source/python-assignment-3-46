numbers = [int(x) for x in input("Enter numbers: ").split()]
value = int(input("Enter element to find: "))
if value in numbers:
    print("Index:", numbers.index(value))
else:
    print("Element not found")
