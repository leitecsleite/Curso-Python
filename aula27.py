# Initialize a dictionary named 'person' with some initial key-value pairs
person = {
    'name': 'Lucas',           # Key 'name' with value 'Lucas'
    'last_name': 'Miranda',    # Key 'last_name' with value 'Miranda'
}

# Update the value associated with the 'name' key to 'Lucas Leite'
key = 'name'                   # Store the key 'name' in variable 'key'
person[key] = 'Lucas Leite'

# Add a new key-value pair 'last_name' with value 'Miranda'
person['last_name'] = 'Miranda'

# Print the updated value associated with the 'name' key
print(person[key])

# Update the value associated with the 'name' key to 'Davi'
person[key] = 'Davi'

# Delete the key 'last_name' and its corresponding value
del person['last_name']

# Print the dictionary 'person' after modifications
print(person)

# Print the value associated with the 'name' key
print(person['name'])

# Check if the key 'last_name' exists in the dictionary using the get() method
if person.get('last_name') is None:
    print('Does not exist')