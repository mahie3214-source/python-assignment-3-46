numbers = [int(x) for x in input("Enter list elements: ").split()]
index = int(input("Enter index to delete: "))
if -len(numbers) <= index < len(numbers):
    removed = numbers.pop(index)
    print("Removed:", removed)
else:
    print("Invalid index")
print(numbers)
