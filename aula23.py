def even_odd(number):
    multiples_of_two = number % 2 == 0

    if multiples_of_two:
        return f'{number} is even'
    else: 
        return f'{number} is odd'

# Call the function with different numbers and print the results
print(even_odd(2))  # Output: 2 is even
print(even_odd(3))  # Output: 3 is odd






