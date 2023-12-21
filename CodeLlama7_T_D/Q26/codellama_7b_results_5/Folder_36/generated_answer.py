
def sum_in_range(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Loop through the list of integers
    for num in my_list:

        # Check if the number is between 465 and 927, both inclusive
        if 465 <= num <= 927:

            # If it is, add it to the sum
            total += num

    # Return the sum
    return total
