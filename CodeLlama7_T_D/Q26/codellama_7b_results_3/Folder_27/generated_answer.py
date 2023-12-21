
def sum_in_range(my_list):
    # Initialize the sum to 0
    total = 0
    # Iterate over the list of integers
    for num in my_list:
        # Check if the number is between 68 and 99, both inclusive
        if 68 <= num <= 99:
            # If it is, add it to the total sum
            total += num

    # Return the total sum
    return total
