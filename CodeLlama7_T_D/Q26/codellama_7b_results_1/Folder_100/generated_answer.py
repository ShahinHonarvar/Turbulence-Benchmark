
def sum_in_range(my_list):
    # Initialize the sum to 0
    total = 0
    # Iterate over the list of integers
    for num in my_list:
        # Check if the number is between 19 and 32, both inclusive
        if 19 <= num <= 32:
            # If it is, add it to the total
            total += num

    # Return the sum
    return total
