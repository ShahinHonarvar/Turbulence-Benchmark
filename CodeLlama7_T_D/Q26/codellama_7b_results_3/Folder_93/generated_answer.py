
def sum_in_range(my_list):
    # Initialize the sum to 0
    total = 0
    # Iterate over the list of integers
    for num in my_list:
        # Check if the number is between -23 and 64, both inclusive
        if -23 <= num <= 64:
            # Add the number to the sum
            total += num

    # Return the sum
    return total
