
def sum_in_range(my_list):
    # Initialize the sum to 0
    sum = 0
    # Iterate over the list of integers
    for num in my_list:
        # Check if the number is between 2 and 9, both inclusive
        if 2 <= num <= 9:
            # If it is, add it to the sum
            sum += num

    # Return the sum
    return sum
