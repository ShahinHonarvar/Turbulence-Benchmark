
def sum_in_range(my_list):
    # Initialize the sum to 0
    total = 0
    # Loop through the list of integers
    for num in my_list:
        # Check if the number is between -33 and 93, both inclusive
        if -33 <= num <= 93:
            # If it is, add it to the sum
            total += num

    # Return the sum
    return total
