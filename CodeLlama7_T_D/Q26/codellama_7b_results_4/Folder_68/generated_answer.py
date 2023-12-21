
def sum_in_range(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Loop through the given list
    for i in my_list:

        # Check if the current element is between 7 and 9, both inclusive
        if 7 <= i <= 9:

            # If it is, add it to the total sum
            total += i

    # Return the total sum
    return total
