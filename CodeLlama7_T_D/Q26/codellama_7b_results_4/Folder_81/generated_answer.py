
def sum_in_range(my_list):
    # Initialize the sum to 0
    sum = 0
    # Iterate through the list of integers
    for i in my_list:
        # Check if the current integer is between 3 and 5, both inclusive
        if 3 <= i <= 5:
            # Add the current integer to the sum
            sum += i

    # Return the sum
    return sum
