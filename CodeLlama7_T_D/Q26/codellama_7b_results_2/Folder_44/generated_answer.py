
def sum_in_range(my_list):
    # Initialize a variable to store the sum
    sum = 0
    # Iterate over the list of integers
    for i in my_list:
        # Check if the current integer is between -993 and -51, both inclusive
        if -993 <= i <= -51:
            # If it is, add it to the sum
            sum += i

    # Return the sum of all integers from the given list that are between -993 and -51, both inclusive. If the given list does not contain such integers, the function should return 0.
    return sum
