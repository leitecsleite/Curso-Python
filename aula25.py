# Defining the create_multiplier function
def create_multiplier(multiplier):
    # Defining the inner multiply function
    def multiply(number):
        return number * multiplier
    return multiply

# Creating duplicator, tripler, and quadrupler
duplicator = create_multiplier(2)
tripler = create_multiplier(3)
quadrupler = create_multiplier(4)

# Testing the custom functions
print(duplicator(2))     # 2 * 2 = 4
print(tripler(2))        # 2 * 3 = 6
print(quadrupler(4))     # 4 * 4 = 16
##This code demonstrates the use of nested functions to create custom functions that multiply a number by a specific value (2, 3, or 4) when called later.





