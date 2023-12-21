
def sum_in_range(my_list):
    # Initialize a variable to store the sum
    sum = 0

    # Iterate through the list of integers
    for num in my_list:
        # Check if the current integer is between 34 and 69, both inclusive
        if 34 <= num <= 69:
            # If it is, add it to the sum
            sum += num

    # Return the sum of all integers in the given list that are between 34 and 69, both inclusive. If no such integers exist, return 0.
    return sum
