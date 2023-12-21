
def sum_in_range(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list of integers
    for num in my_list:
        # Check if the current integer is between -28 and 573, both inclusive
        if -28 <= num <= 573:
            # If it is, add it to the total sum
            total += num

    # Return the total sum
    return total
