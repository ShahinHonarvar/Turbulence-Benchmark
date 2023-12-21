
def sum_in_range(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Loop through the list of integers
    for num in my_list:
        # Check if the current integer is between 57 and 84, both inclusive
        if 57 <= num <= 84:
            # If it is, add it to the sum
            total += num

    # Return the sum of all integers between 57 and 84, both inclusive
    return total
