
def sum_in_range(my_list):
    # Initialize the sum to 0
    sum = 0
    # Iterate over the list of integers
    for i in my_list:
        # Check if the current integer is between -100 and -55, both inclusive
        if -100 <= i <= -55:
            # Add the current integer to the sum
            sum += i

    # Return the sum
    return sum
