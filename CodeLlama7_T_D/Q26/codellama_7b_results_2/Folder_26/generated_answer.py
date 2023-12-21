
def sum_in_range(my_list):
    # Initialize the sum to 0
    total = 0

    # Loop through the list of integers
    for num in my_list:
        # Check if the current integer is between -355 and -297, both inclusive
        if (-355 <= num <= -297):
            # If it is, add it to the total sum
            total += num

    # Return the total sum
    return total
