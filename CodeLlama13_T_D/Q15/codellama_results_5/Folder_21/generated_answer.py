
def sum_odd_ints_inclusive(numbers):
    # Initialize a variable to store the sum
    sum = 0
    
    # Iterate through the list of integers
    for i in range(639, 975 + 1):
        # Check if the current integer is odd
        if numbers[i] % 2 == 1:
            # Add it to the sum
            sum += numbers[i]
    
    # Return the sum
    return sum
