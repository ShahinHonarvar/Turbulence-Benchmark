
def sum_in_range(my_list):
    # Initialize the sum to 0
    total = 0
    # Loop through the list of integers
    for num in my_list:
        # Check if the current integer is between 682 and 744, both inclusive
        if 682 <= num <= 744:
            # If it is, add it to the sum
            total += num

    # Return the sum
    return total
