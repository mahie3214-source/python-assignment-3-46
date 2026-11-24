original = [1, 2, 3]
assigned = original
copied = original.copy()
original.append(4)
print("Original:", original)
print("Direct assignment:", assigned)
print("Using copy():", copied)
