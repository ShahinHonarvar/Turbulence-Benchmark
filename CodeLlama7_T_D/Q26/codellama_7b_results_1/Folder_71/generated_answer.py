
def sum_in_range(my_list):
    # Initialize a variable to store the sum
    sum = 0

    # Iterate through the given list of integers
    for num in my_list:
        # Check if the current integer is between 39 and 43, both inclusive
        if 39 <= num <= 43:
            # If it is, add it to the sum
            sum += num

    # Return the sum of all integers from the given list that are between 39 and 43, both inclusive. If the given list does not contain such integers, the function should return 0.
    return sum
