import random

def generate_random_list():
    """Generate a list of 10 random integers between 1 and 50."""
    random_numbers = []
    for _ in range(10):  # Repeat 10 times to get 10 numbers
        number = random.randint(1, 50)  # Choose a random number between 1 and 50
        random_numbers.append(number)  # Add it to the list
    return random_numbers

def substitute(numbers):
    """Change numbers in the list that are multiples of 5 to their squares."""
    modified_numbers = []
    for number in numbers:
        if number % 5 == 0:  # Check if the number is a multiple of 5
            modified_numbers.append(number ** 2)  # If true, add its square to the new list
        else:
            modified_numbers.append(number)  # Otherwise, add the number as it is
    return modified_numbers

# Generate the random list of numbers
original_list = generate_random_list()
print("Original list:", original_list)

# Create a new list with certain numbers squared
new_list = substitute(original_list)
print("Modified list:", new_list)