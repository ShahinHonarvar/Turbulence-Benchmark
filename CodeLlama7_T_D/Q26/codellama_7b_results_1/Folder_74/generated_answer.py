
def sum_in_range(my_list):
    # Initialize the sum to 0
    sum = 0
    # Iterate over the list of integers
    for i in my_list:
        # Check if the integer is between 13 and 35, both inclusive
        if 13 <= i <= 35:
            # Add the integer to the sum
            sum += i

    return sum
