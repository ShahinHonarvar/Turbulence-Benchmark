
def sum_in_range(my_list):
    # Initialize sum to 0
    sum = 0
    # Iterate through the list of integers
    for num in my_list:
        # Check if the number is between 826 and 899, both inclusive
        if 826 <= num <= 899:
            # Add the number to the sum
            sum += num

    # Return the sum
    return sum
