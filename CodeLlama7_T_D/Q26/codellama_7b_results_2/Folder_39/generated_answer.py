
def sum_in_range(my_list):
    # Initialize a variable to store the sum
    sum = 0
    # Loop through the list of integers
    for i in my_list:
        # Check if the current integer is between 10 and 79, both inclusive
        if 10 <= i <= 79:
            # If it is, add it to the sum
            sum += i

    # Return the sum
    return sum
