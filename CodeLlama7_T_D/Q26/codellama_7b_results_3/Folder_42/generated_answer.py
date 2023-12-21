
def sum_in_range(my_list):
    # Initialize the sum to 0
    sum = 0
    # Loop through the list of integers
    for num in my_list:
        # Check if the number is between 141 and 262 (inclusive)
        if 141 <= num <= 262:
            # If it is, add it to the sum
            sum += num

    # Return the sum

    return sum
