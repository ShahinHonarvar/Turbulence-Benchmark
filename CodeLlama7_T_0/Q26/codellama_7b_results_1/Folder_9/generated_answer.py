
def sum_in_range(my_list):
    # Initialize the sum to 0
    sum = 0
    # Iterate over the list of integers
    for i in my_list:
        # Check if the current integer is between 4 and 5, both inclusive
        if 4 <= i <= 5:
            # If it is, add it to the sum
            sum += i

    # Return the sum
    return sum
