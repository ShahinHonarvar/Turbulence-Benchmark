
def sum_in_range(my_list):
    # Initialize sum to 0
    sum = 0
    # Iterate through the list of integers
    for i in my_list:
        # Check if the integer is between 514 and 816, both inclusive
        if 514 <= i <= 816:
            # If it is, add it to the sum
            sum += i

    # Return the sum
    return sum
