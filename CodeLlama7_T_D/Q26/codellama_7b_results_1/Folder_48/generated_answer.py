
def sum_in_range(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Loop through the list of integers
    for num in my_list:

        # Check if the number is between 827 and 999, both inclusive
        if 827 <= num <= 999:

            # If it is, add it to the sum
            total += num

    # Return the sum
    return total
