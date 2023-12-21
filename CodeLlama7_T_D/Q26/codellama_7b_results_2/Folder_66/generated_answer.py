
def sum_in_range(my_list):
    # Initialize the sum to 0
    sum = 0
    # Iterate through the list of integers
    for i in my_list:
        # Check if the integer is between 28 and 96, both inclusive
        if 28 <= i <= 96:
            # Add the integer to the sum
            sum += i

    # Return the sum
    return sum
