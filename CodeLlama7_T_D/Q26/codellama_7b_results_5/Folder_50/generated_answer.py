
def sum_in_range(my_list):
    # Initialize a variable to store the sum
    sum = 0

    # Iterate through the given list
    for i in my_list:

        # Check if the current element is between 34 and 69, both inclusive
        if 34 <= i <= 69:

            # If it is, add it to the sum
            sum += i

    # Return the sum
    return sum
