
def sum_in_range(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate over the given list of integers
    for num in my_list:
        # Check if the current integer is between 2 and 7, both inclusive
        if 2 <= num <= 7:
            # If it is, add it to the total sum
            total += num

    # Return the total sum of all integers between 2 and 7, both inclusive
    return total
