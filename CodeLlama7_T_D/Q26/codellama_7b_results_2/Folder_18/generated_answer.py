
def sum_in_range(my_list):
    # Initialize sum to 0
    sum = 0
    # Loop through the list of integers
    for num in my_list:
        # Check if the number is between 826 and 899, both inclusive
        if 826 <= num <= 899:
            # If the number is between the specified range, add it to the sum
            sum += num

    # Return the sum of all integers from the given list that are between 826 and 899, both inclusive. If the given list does not contain such integers, the function should return 0.
    return sum
