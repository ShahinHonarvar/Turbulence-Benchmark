
def sum_in_range(my_list):
    # Initialize the sum to 0
    sum = 0
    # Iterate through the list of integers
    for i in my_list:
        # Check if the current integer is between -74 and -17, both inclusive
        if -74 <= i <= -17:
            # If it is, add it to the sum
            sum += i

    # Return the sum

    return sum
