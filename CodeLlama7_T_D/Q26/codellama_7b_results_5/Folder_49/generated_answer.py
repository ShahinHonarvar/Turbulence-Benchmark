
def sum_in_range(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Loop through the list of integers
    for num in my_list:
        # Check if the current integer is between 3 and 9, both inclusive
        if 3 <= num <= 9:
            # If it is, add it to the sum
            total += num

    # Return the sum of all integers from the given list that are between 3 and 9, both inclusive. If the given list does not contain such integers, the function should return 0.
    return total
