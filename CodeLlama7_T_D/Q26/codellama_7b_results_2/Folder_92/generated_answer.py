
def sum_in_range(my_list):
    # Initialize the sum to 0
    total = 0

    # Iterate over the list of integers
    for num in my_list:
        # Check if the current number is between 5 and 9, both inclusive
        if 5 <= num <= 9:
            # If it is, add it to the total sum
            total += num

    # Return the total sum
    return total
