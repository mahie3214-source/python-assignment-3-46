numbers = [int(x) for x in input("Enter numbers: ").split()]
print("Ascending:", sorted(numbers))
print("Descending:", sorted(numbers, reverse=True))
