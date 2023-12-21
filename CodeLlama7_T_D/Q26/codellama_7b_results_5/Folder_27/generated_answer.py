
def sum_in_range(my_list):
    # Initialize the sum to 0
    total = 0
    # Loop through the list of integers
    for i in my_list:
        # Check if the current integer is between 68 and 99, both inclusive
        if 68 <= i <= 99:
            # If it is, add it to the sum
            total += i

    # Return the sum
    return total
