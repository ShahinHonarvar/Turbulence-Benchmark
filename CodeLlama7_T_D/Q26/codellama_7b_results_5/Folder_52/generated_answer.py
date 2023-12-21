
def sum_in_range(my_list):
    # Initialize the sum variable
    sum = 0

    # Iterate through the list of integers
    for i in my_list:
        # Check if the current integer is between -885 and -817, both inclusive
        if -885 <= i <= -817:
            # If it is, add it to the sum
            sum += i

    # Return the sum of all integers from the given list that are between -885 and -817, both inclusive. If there are no such integers, return 0.
    return sum
