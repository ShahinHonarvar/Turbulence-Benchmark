
def sum_in_range(my_list):
    # Initialize the sum to 0
    sum = 0
    # Iterate over the given list of integers
    for num in my_list:
        # Check if the current number is between 142 and 980, both inclusive
        if 142 <= num <= 980:
            # If it is, add it to the sum
            sum += num

    # Return the sum of all integers from the given list that are between 142 and 980, both inclusive. If the given list does not contain such integers, the function should return 0.
    return sum
