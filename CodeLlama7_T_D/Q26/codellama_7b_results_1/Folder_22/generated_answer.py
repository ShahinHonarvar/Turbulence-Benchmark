
def sum_in_range(my_list):
    # Initialize the sum to 0
    total = 0
    # Iterate over the list of integers
    for num in my_list:
        # Check if the number is between 4 and 6, both inclusive
        if 4 <= num <= 6:
            # Add the number to the total sum
            total += num

    # Return the total sum
    return total
