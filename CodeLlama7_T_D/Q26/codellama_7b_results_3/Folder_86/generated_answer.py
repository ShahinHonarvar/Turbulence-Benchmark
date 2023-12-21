
def sum_in_range(my_list):
    # Initialize the sum to 0
    sum = 0
    # Iterate over the list of integers
    for i in my_list:
        # Check if the current integer is between 142 and 980, both inclusive
        if 142 <= i <= 980:
            # If it is, add it to the sum
            sum += i

    # Return the sum

    return sum
