
def sum_in_range(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate over the list of integers
    for num in my_list:

        # Check if the current integer is between -23 and 64, both inclusive
        if -23 <= num <= 64:

            # If it is, add it to the total sum
            total += num

    # Return the total sum
    return total
