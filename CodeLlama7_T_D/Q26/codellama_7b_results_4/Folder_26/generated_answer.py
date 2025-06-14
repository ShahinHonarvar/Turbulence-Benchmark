
def sum_in_range(my_list):
    # Initialize sum to 0
    sum = 0
    # Iterate over the list of integers
    for i in my_list:
        # Check if the current integer is between -355 and -297, both inclusive
        if -355 <= i <= -297:
            # If it is, add it to the sum
            sum += i

    # Return the sum
    return sum
