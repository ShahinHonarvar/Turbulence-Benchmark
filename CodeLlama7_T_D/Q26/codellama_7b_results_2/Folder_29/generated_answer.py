
def sum_in_range(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Loop through the list of integers
    for num in my_list:
        # Check if the current integer is between 18 and 60, both inclusive
        if 18 <= num <= 60:
            # If it is, add it to the sum
            total += num

    # Return the sum of all integers from the given list that are between 18 and 60, both inclusive. If the given list does not contain such integers, the function should return 0.
    return total
