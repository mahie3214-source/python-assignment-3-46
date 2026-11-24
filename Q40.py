first = [int(x) for x in input("Enter first list: ").split()]
second = [int(x) for x in input("Enter second list: ").split()]
common = []
for item in first:
    if item in second and item not in common:
        common.append(item)
print("Common elements:", common)
