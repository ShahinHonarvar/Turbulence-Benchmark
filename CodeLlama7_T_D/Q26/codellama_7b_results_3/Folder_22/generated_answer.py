
def sum_in_range(my_list):
    # Initialize the sum variable
    sum = 0
    # Iterate over the list of integers
    for num in my_list:
        # Check if the current number is between 4 and 6 (both inclusive)
        if 4 <= num <= 6:
            # Add the current number to the sum
            sum += num

    return sum
