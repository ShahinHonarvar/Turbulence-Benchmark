
def sum_in_range(my_list):
    # Initialize a variable to store the sum
    sum = 0
    # Loop through the list of integers
    for i in my_list:
        # Check if the current integer is between 86 and 99, both inclusive
        if 86 <= i <= 99:
            # Add the current integer to the sum
            sum += i

    # Return the sum
    return sum
