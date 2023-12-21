
def sum_in_range(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Loop through the list of integers
    for num in my_list:

        # Check if the number is between 28 and 96, inclusive
        if 28 <= num <= 96:

            # If it is, add it to the total
            total += num

# Return the sum of all integers in the given list that are between 28 and 96, inclusive. If there are no such integers, return 0.
    return total
