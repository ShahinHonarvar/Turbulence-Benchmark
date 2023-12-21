
def sum_in_range(my_list):
    # Initialize the sum to 0
    sum = 0
    # Loop through the list of integers
    for i in my_list:
        # Check if the current integer is between 3 and 4, both inclusive
        if 3 <= i <= 4:
            # Add the current integer to the sum
            sum += i

    return sum
