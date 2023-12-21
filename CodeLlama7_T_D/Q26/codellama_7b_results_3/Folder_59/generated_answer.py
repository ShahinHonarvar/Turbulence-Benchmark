
def sum_in_range(my_list):
    # Initialize sum to 0
    sum = 0
    # Loop through the list of integers
    for i in my_list:
        # Check if the current integer is between 2 and 3, both inclusive
        if 2 <= i <= 3:
            # If it is, add it to the sum
            sum += i

    # Return the sum
    return sum
