
def sum_in_range(my_list):
    # Initialize the sum to 0
    sum = 0
    # Loop through the list of integers
    for i in my_list:
        # Check if the current integer is between 20 and 93, both inclusive
        if 20 <= i <= 93:
            # Add the current integer to the sum
            sum += i

    # Return the sum of all integers between 20 and 93, both inclusive
    return sum
