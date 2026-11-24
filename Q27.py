items = input("Enter list elements separated by spaces: ").split()
if items:
    print("First:", items[0])
    print("Last:", items[-1])
    print("Middle:", items[len(items) // 2])
else:
    print("List is empty")
