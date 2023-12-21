
def sum_in_range(my_list):
    # Initialize the sum to 0
    total = 0
    # Loop through the list of integers
    for i in my_list:
        # Check if the current integer is between 335 and 611, both inclusive
        if 335 <= i <= 611:
            # If it is, add it to the total sum
            total += i

    # Return the total sum

    return total
