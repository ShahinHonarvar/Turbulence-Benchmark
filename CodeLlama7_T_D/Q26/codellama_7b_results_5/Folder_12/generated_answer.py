
def sum_in_range(my_list):
    # Initialize the sum to 0
    sum = 0
    # Iterate over the list of integers
    for i in my_list:
        # Check if the integer is between -91 and -61, both inclusive
        if -91 <= i <= -61:
            # If it is, add it to the sum
            sum += i

    # Return the sum
    return sum
