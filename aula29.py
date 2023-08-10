import copy

# Create an original dictionary called d1
d1 = {
    "c1": 1,
    "c2": 2,
    "li": [0, 1, 2, 3]
}

# Create a deep copy of d1 and assign it to d2
d2 = copy.deepcopy(d1)

# Modify the value associated with the key 'c1' in d2
d2['c1'] = 1000

# Modify the second element of the list associated with the key 'li' in d2
d2['li'][1] = 999999

# Print the content of d1 (original) and d2 (modified copy)
print("d1:")
print(d1)
print("\nd2:")
print(d2)