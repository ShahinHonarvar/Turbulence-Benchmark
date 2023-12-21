
def sum_in_range(my_list):
    # Initialize the sum to 0
    total = 0

    # Loop through the list of integers
    for num in my_list:
        # Check if the current number is between 4 and 6, both inclusive
        if 4 <= num <= 6:
            # If it is, add it to the sum
            total += num

    # Return the sum
    return total
