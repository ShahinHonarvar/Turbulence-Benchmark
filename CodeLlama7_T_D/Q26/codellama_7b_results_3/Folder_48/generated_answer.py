
def sum_in_range(my_list):
    # Initialize the sum to 0
    sum = 0
    # Iterate over the list of integers
    for num in my_list:
        # Check if the number is between 827 and 999, inclusive
        if 827 <= num <= 999:
            # If the number is between the specified range, add it to the sum
            sum += num

    # Return the sum of all integers from the given list that are between 827 and 999, both inclusive. If the given list does not contain such integers, the function should return 0.
    return sum
