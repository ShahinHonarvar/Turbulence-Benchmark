
def sum_in_range(my_list):
    # Initialize a variable to store the sum
    sum = 0
    # Iterate through the list of integers
    for num in my_list:
        # Check if the current integer is between 18 and 60 (inclusive)
        if 18 <= num <= 60:
            # If it is, add it to the sum
            sum += num

    # Return the sum of all integers from the given list that are between 18 and 60 (inclusive). If there are no such integers, return 0.
    return sum
