
def sum_in_range(my_list):
    # Initialize the sum variable
    sum = 0
    # Loop through the list of integers
    for i in my_list:
        # Check if the integer is between 682 and 744, both inclusive
        if 682 <= i <= 744:
            # Add the integer to the sum
            sum += i

    return sum
