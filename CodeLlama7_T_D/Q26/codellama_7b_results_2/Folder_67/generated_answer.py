
def sum_in_range(my_list):
    # Initialize the sum to 0
    sum = 0
    # Loop through the list of integers
    for i in my_list:
        # Check if the integer is between 31 and 50, both inclusive
        if 31 <= i <= 50:
            # If it is, add it to the sum
            sum += i

    # Return the sum
    return sum
