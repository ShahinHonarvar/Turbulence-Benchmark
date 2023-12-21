
def sum_in_range(my_list):
    # Initialize the sum to 0
    sum = 0
    # Iterate through the list of integers
    for num in my_list:
        # Check if the current number is between 57 and 84, both inclusive
        if 57 <= num <= 84:
            # If it is, add it to the sum
            sum += num

    # Return the sum

    return sum
