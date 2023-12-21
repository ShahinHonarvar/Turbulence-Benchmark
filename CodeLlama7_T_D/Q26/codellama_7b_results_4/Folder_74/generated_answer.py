
def sum_in_range(my_list):
    # Initialize the sum variable
    sum = 0

    # Iterate over the list of integers
    for i in my_list:
        # Check if the current integer is between 13 and 35, both inclusive
        if 13 <= i <= 35:
            # Add the current integer to the sum variable
            sum += i

    # Return the sum of all integers from the given list that are between 13 and 35, both inclusive. If there are no such integers, return 0.
    return sum
