
def sum_in_range(my_list):
    # Initialize the sum variable
    sum = 0

    # Loop through the list of integers
    for i in my_list:

        # Check if the current integer is between 3 and 5, both inclusive
        if 3 <= i <= 5:

            # Add the current integer to the sum
            sum += i

    # Return the sum of all integers between 3 and 5, both inclusive
    return sum
