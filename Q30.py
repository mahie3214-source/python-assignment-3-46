numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
even = sum(1 for n in numbers if n % 2 == 0)
odd = len(numbers) - even
print("Even elements:", even)
print("Odd elements:", odd)
