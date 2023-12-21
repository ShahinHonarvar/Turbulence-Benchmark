
def sum_in_range(my_list):
    # Initialize the sum variable
    sum = 0

    # Loop through the list of integers
    for i in my_list:
        # Check if the integer is between 138 and 858, both inclusive
        if 138 <= i <= 858:
            # If it is, add it to the sum
            sum += i

    # Return the sum
    return sum
