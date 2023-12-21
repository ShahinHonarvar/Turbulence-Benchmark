
def sum_in_range(my_list):
    # Initialize a variable to store the sum
    sum = 0
    # Loop through the list of integers
    for i in my_list:
        # Check if the current integer is between 3 and 6, both inclusive
        if 3 <= i <= 6:
            # If it is, add it to the sum
            sum += i

    # Return the sum
    return sum
