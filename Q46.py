items = tuple(input("Enter tuple elements separated by spaces: ").split())
if items:
    print("Tuple:", items)
    print("First element:", items[0])
    print("Last element:", items[-1])
else:
    print("Tuple is empty")
