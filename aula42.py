# Creating a list using list comprehension to store coordinate tuples
lista = [
    (x, y)                  # Tuple containing x and y
    for x in range(3)       # Loop through x values from 0 to 2
    for y in range(3)       # Loop through y values from 0 to 2 for each x
]

# Printing the generated list of coordinate tuples
print(lista)