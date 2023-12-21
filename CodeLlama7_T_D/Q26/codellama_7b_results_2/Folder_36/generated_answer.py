
def sum_in_range(my_list):
    # Initialize the sum to 0
    sum = 0
    # Iterate through the list of integers
    for i in my_list:
        # Check if the integer is between 465 and 927, both inclusive
        if 465 <= i <= 927:
            # If it is, add it to the sum
            sum += i

    # Return the sum
    return sum
