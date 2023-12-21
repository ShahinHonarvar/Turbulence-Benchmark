
def sum_in_range(my_list):
    # Initialize a variable to store the sum
    sum = 0
    # Iterate through the list of integers
    for i in my_list:
        # Check if the current integer is between 90 and 97, both inclusive
        if 90 <= i <= 97:
            # If it is, add it to the sum
            sum += i

    # Return the sum
    return sum
