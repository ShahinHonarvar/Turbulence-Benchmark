
def sum_in_range(my_list):
    # Initialize the sum to 0
    total = 0
    # Iterate through the list of integers
    for i in my_list:
        # Check if the current integer is between 34 and 69, both inclusive
        if 34 <= i <= 69:
            # Add the current integer to the sum
            total += i

    # Return the sum

    return total
