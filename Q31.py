numbers = [int(x) for x in input("Enter list elements: ").split()]
value = int(input("Enter element to insert: "))
position = int(input("Enter position (index): "))
numbers.insert(position, value)
print(numbers)
