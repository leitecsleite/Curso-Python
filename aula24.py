# Define a function that creates personalized greetings
def create_greeting(greeting):
    # Define a nested function that takes a name and combines it with the given greeting
    def greet(name):
        return f'{greeting}, {name}!'
    return greet  # Return the nested function

# Create greeting functions for "Good morning" and "Good night"
say_good_morning = create_greeting('Good morning')
say_good_night = create_greeting('Good night')

# Loop through a list of names and use the created greeting functions
for name in ['Maria', 'Joana', 'Luiz']:
    # Call the "Good morning" greeting function and print the result
    print(say_good_morning(name))
    
    # Call the "Good night" greeting function and print the result
    print(say_good_night(name))