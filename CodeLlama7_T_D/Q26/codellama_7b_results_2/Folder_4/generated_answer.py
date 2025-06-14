
def sum_in_range(my_list):
    # Initialize the sum variable
    total = 0

    # Loop through the list of integers
    for num in my_list:
        # Check if the current integer is between 32 and 44 (inclusive)
        if 32 <= num <= 44:
            # If it is, add it to the total sum
            total += num

    # Return the total sum
    return total
