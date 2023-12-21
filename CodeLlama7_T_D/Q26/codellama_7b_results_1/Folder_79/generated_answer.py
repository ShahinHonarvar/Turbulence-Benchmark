
def sum_in_range(my_list):
    # Initialize sum to 0
    sum = 0

    # Iterate through the list of integers
    for num in my_list:
        # Check if the current integer is between 2 and 9, both inclusive
        if (num >= 2) and (num <= 9):
            # If it is, add it to the sum
            sum += num

    # Return the sum of all integers from the given list that are between 2 and 9, both inclusive. If the given list does not contain such integers, return 0.
    return sum
