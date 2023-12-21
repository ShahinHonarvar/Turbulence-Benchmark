
def sum_in_range(my_list):
    # Initialize sum to 0
    sum = 0
    # Loop through the list of integers
    for num in my_list:
        # Check if the number is between 138 and 858, inclusive
        if (num >= 138 and num <= 858):
            # If it is, add it to the sum
            sum += num

    # Return the sum
    return sum
