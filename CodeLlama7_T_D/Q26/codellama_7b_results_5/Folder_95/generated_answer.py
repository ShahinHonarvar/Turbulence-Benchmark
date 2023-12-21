
def sum_in_range(my_list):
    # Initialize the sum to 0
    total = 0
    # Loop through the list of integers
    for num in my_list:
        # Check if the number is between 43 and 70, both inclusive
        if 43 <= num <= 70:
            # If it is, add it to the sum
            total += num

    # Return the sum
    return total
