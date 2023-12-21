
def sum_in_range(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list of integers
    for num in my_list:

        # Check if the current number is between 6 and 8, both inclusive
        if 6 <= num <= 8:

            # If it is, add it to the sum
            total += num

    # Return the sum
    return total
