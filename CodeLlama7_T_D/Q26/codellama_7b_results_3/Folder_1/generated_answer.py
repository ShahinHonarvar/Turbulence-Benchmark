
def sum_in_range(my_list):
    # Initialize the sum variable to 0
    sum = 0
    # Iterate through the list of integers
    for i in my_list:
        # Check if the current integer is between -97 and -48, both inclusive
        if -97 <= i <= -48:
            # If it is, add it to the sum
            sum += i

    # Return the sum of all integers from the given list that are between -97 and -48, both inclusive. If the given list does not contain such integers, the function should return 0.
    return sum
