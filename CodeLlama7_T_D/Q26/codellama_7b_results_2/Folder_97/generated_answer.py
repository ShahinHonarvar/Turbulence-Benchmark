
def sum_in_range(my_list):
    # Initialize the sum variable
    sum = 0

    # Loop through the list of integers
    for i in my_list:
        # Check if the current integer is between 584 and 619, both inclusive
        if 584 <= i <= 619:
            # If it is, add it to the sum variable
            sum += i

    # Return the sum of all integers in the given list that are between 584 and 619, both inclusive. If the list does not contain such integers, return 0.
    return sum
