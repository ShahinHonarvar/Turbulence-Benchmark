
def sum_in_range(my_list):
    # Initialize a variable to store the sum
    sum = 0
    # Iterate over the list of integers
    for i in my_list:
        # Check if the current integer is between 3 and 4, both inclusive
        if 3 <= i <= 4:
            # If it is, add it to the sum
            sum += i

    # Return the sum
    return sum
