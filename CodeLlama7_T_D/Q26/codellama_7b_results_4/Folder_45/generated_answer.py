
def sum_in_range(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Loop through the list of integers
    for num in my_list:
        # Check if the current number is between 3 and 4 (inclusive)
        if 3 <= num <= 4:
            # Add the current number to the total sum
            total += num

    # Return the total sum
    return total
