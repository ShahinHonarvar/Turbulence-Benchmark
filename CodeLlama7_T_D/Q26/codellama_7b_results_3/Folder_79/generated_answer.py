
def sum_in_range(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate over the list of integers
    for num in my_list:
        # Check if the number is between 2 and 9, both inclusive
        if 2 <= num <= 9:
            # Add the number to the total
            total += num

    # Return the sum
    return total
