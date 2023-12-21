
def sum_in_range(my_list):
    # Initialize the sum variable
    sum = 0

    # Loop through the list of integers
    for i in my_list:
        # Check if the current integer is between 44 and 67, both inclusive
        if 44 <= i <= 67:
            # If it is, add it to the sum
            sum += i

    # Return the sum
    return sum
