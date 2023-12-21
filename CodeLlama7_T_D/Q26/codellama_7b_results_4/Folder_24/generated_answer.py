
def sum_in_range(my_list):
    # Initialize the sum to 0
    total = 0
    # Loop through the list of integers
    for num in my_list:
        # Check if the number is between -91 and -41, both inclusive
        if -91 <= num <= -41:
            # If it is, add it to the sum
            total += num

    # Return the sum
    return total
