
def sum_in_range(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate over the list of integers
    for num in my_list:

        # Check if the current integer is between 4 and 6, both inclusive
        if 4 <= num <= 6:

            # If it is, add it to the total sum
            total += num

    # Return the total sum
    return total
