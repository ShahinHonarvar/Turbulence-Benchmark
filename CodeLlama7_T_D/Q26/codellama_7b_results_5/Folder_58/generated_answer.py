
def sum_in_range(my_list):
    # Initialize the sum variable
    sum = 0

    # Loop through the list of integers
    for i in my_list:
        # Check if the current integer is between 514 and 816, both inclusive
        if (514 <= i) and (i <= 816):
            # If it is, add it to the sum
            sum += i

    # Return the sum of all integers between 514 and 816, both inclusive
    return sum
