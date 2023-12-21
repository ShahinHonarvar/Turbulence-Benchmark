
def sum_in_range(my_list):
    # Initialize the sum to 0
    sum = 0
    # Loop through the list of integers
    for num in my_list:
        # Check if the number is between -74 and -17, both inclusive
        if -74 <= num <= -17:
            # If it is, add it to the sum
            sum += num

    # Return the sum
    return sum
