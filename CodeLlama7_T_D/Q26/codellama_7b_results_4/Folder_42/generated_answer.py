
def sum_in_range(my_list):
    # Initialize the sum to 0
    sum = 0
    # Iterate over the list of integers
    for i in my_list:
        # Check if the integer is between 141 and 262, both inclusive
        if 141 <= i <= 262:
            # If it is, add it to the sum
            sum += i

    # Return the sum

    return sum
