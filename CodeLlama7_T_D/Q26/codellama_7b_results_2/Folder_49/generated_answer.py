
def sum_in_range(my_list):
    # Initialize the sum to 0
    sum = 0
    # Loop through the list of integers
    for num in my_list:
        # Check if the number is between 3 and 9, both inclusive
        if (num >= 3) and (num <= 9):
            # Add the number to the sum
            sum += num

    # Return the sum
    return sum
