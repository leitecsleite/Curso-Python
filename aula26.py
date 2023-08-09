# Defining a dictionary called 'person'
person = {
    'first_name': 'Lucas',      # Key 'first_name' with value 'Lucas'
    'last_name': 'Miranda',     # Key 'last_name' with value 'Miranda'
    'age': 18,                  # Key 'age' with value 18
    'height': 1.8,              # Key 'height' with value 1.8
    'address': [                # Key 'address' with a list of dictionaries
        {'street': 'tal tal', 'number': 123},  # Dictionary 1 with keys 'street' and 'number'
        {'street': 'tal tal', 'number': 123},  # Dictionary 2 with keys 'street' and 'number'
    ]
}

# Printing the entire dictionary, along with its type
print(person, type(person))

# Accessing and printing the value associated with the 'first_name' key
print(person['first_name'])

print()  # Print a blank line for separation

# Iterating through the keys in the 'person' dictionary
for key in person:
    # Printing each key and its corresponding value
    print(key, person[key])