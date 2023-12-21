
def sum_in_range(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Loop through the given list of integers
    for num in my_list:

        # Check if the current integer is between -33 and 93, both inclusive
        if -33 <= num <= 93:

            # If it is, add it to the total sum
            total += num

    # Return the total sum
    return total
