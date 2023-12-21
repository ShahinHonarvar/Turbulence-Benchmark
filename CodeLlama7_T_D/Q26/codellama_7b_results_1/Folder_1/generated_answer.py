
def sum_in_range(my_list):
    # Initialize a variable to store the sum
    sum = 0

    # Loop through the list of integers
    for i in my_list:
        # Check if the integer is between -97 and -48, both inclusive
        if -97 <= i <= -48:
            # If it is, add it to the sum
            sum += i

    # Return the sum
    return sum
