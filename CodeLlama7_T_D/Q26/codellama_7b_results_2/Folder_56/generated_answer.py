
def sum_in_range(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Loop through the list of integers
    for num in my_list:
        # Check if the number is between 4 and 9, both inclusive
        if 4 <= num <= 9:
            # If it is, add it to the total
            total += num

    # Return the sum
    return total
