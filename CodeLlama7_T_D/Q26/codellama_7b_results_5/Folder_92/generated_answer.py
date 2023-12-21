
def sum_in_range(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate over the list of integers
    for num in my_list:
        # Check if the number is between 5 and 9, both inclusive
        if 5 <= num <= 9:
            # If it is, add it to the sum
            total += num

    # Return the sum
    return total
