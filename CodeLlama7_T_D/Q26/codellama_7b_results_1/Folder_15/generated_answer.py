
def sum_in_range(my_list):
    # Initialize the sum to 0
    sum = 0
    # Iterate over the list of integers
    for i in my_list:
        # Check if the current integer is between 6 and 9, both inclusive
        if 6 <= i <= 9:
            # If it is, add it to the sum
            sum += i

    # Return the sum
    return sum
