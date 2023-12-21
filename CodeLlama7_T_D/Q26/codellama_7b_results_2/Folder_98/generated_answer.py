
def sum_in_range(my_list):
    # Initialize sum to 0
    sum = 0
    # Iterate through the list of integers
    for num in my_list:
        # Check if the current number is between 3 and 8, both inclusive
        if 3 <= num <= 8:
            # If it is, add it to the sum
            sum += num

    # Return the sum
    return sum
