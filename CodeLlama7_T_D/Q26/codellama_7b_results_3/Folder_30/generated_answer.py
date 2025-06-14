
def sum_in_range(my_list):
    # Initialize the sum to 0
    total = 0
    # Iterate through the list of integers
    for num in my_list:
        # Check if the number is between 86 and 90, both inclusive
        if 86 <= num <= 90:
            # Add the number to the sum
            total += num

    # Return the sum
    return total
