
def sum_in_range(my_list):
    # Initialize the sum to 0
    sum = 0
    # Iterate through the list of integers
    for i in my_list:
        # Check if the current integer is between 77 and 84, both inclusive
        if 77 <= i <= 84:
            # Add the current integer to the sum
            sum += i

    # Return the sum
    return sum
