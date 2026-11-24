numbers = [int(x) for x in input("Enter numbers: ").split()]
unique = sorted(set(numbers), reverse=True)
if len(unique) >= 2:
    print("Second largest:", unique[1])
else:
    print("Second largest element does not exist")
