# Function to input integers from the user
def input_integers():
    integers = []
    
    while True:
        user_input = input("Enter an integer (blank to quit): ")
        if user_input == "":
            break
        integers.append(int(user_input))
    return integers

def main():
    # Call the input_integers method to get the list of integers
    integer_list = input_integers()

    # Initialize lists to store positive, zero, and negative numbers
    positives = []
    zeros = []
    negatives = []

    # Separate positive, zero, and negative numbers
    for num in integer_list:
        if num > 0:
            positives.append(num)
        elif num == 0:
            zeros.append(num)
        elif num < 0:
            negatives.append(num)
            
    print()
    print("The numbers were:")
    # Display first positive numbers, then zeros, then negative numbers
    output_list = positives + zeros + negatives
    
    # For loop to print each integers in the list, and on the same line
    for num in output_list:
        print(num, end=" ")

if __name__ == "__main__":
    main()