
def sum_in_range(my_list):
    # Initialize a variable to store the sum
    total = 0
    # Loop through the given list of integers
    for num in my_list:
        # Check if the current integer is between 28 and 96, both inclusive
        if 28 <= num <= 96:
            # If it is, add it to the total sum
            total += num

    # Return the total sum of all integers between 28 and 96, both inclusive
    return total
