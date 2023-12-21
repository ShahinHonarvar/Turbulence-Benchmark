
def sum_in_range(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate over the list of integers
    for num in my_list:
        # Check if the number is between 1 and 8, both inclusive
        if 1 <= num <= 8:
            # If it is, add it to the sum
            total += num

    # Return the sum
    return total
