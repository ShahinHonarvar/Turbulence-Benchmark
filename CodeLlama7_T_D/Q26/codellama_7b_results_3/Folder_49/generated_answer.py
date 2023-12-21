
def sum_in_range(my_list):
    # Initialize the sum to 0
    sum = 0
    # Iterate through the list of integers
    for num in my_list:
        # Check if the current integer is between 3 and 9, inclusive
        if 3 <= num <= 9:
            # If it is, add it to the sum
            sum += num

    # Return the sum
    return sum
