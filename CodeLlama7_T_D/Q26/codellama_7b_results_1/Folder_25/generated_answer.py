
def sum_in_range(my_list):
    # Initialize the sum to 0
    total = 0

    # Loop through the list of integers
    for num in my_list:
        # Check if the number is between -10 and 48, both inclusive
        if -10 <= num <= 48:
            # If it is, add it to the total
            total += num

    # Return the sum
    return total
