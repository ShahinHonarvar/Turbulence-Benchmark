
def sum_in_range(my_list):
    # Initialize the sum to 0
    sum = 0
    # Iterate over the list of integers
    for num in my_list:
        # Check if the number is between 6 and 8, both inclusive
        if 6 <= num <= 8:
            # Add the number to the sum
            sum += num

    # Return the sum
    return sum
