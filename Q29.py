numbers = [float(x) for x in input("Enter numbers separated by spaces: ").split()]
if numbers:
    print("Sum:", sum(numbers))
    print("Average:", sum(numbers) / len(numbers))
else:
    print("List is empty")
