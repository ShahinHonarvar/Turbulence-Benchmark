
def sum_in_range(my_list):
    # Initialize a variable to store the sum
    sum = 0

    # Iterate over the given list of integers
    for i in my_list:
        # Check if the current integer is between -23 and 64, both inclusive
        if -23 <= i <= 64:
            # If it is, add it to the sum
            sum += i

    # Return the sum of all integers from the given list that are between -23 and 64, both inclusive. If there are no such integers, return 0.
    return sum
