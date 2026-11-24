numbers = [int(x) for x in input("Enter numbers: ").split()]
print("Full list:", numbers)
print("First three:", numbers[:3])
print("From index 2:", numbers[2:])
print("Every second element:", numbers[::2])
print("Reversed:", numbers[::-1])
