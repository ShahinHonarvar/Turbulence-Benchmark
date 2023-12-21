
def sum_in_range(my_list):
    # Initialize a variable to store the sum
    sum = 0

    # Iterate over the list of integers
    for i in my_list:
        # Check if the current integer is between 142 and 407, both inclusive
        if 142 <= i <= 407:
            # If it is, add it to the sum
            sum += i

    # Return the sum
    return sum
