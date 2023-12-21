 def sum_in_range(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Loop through the list of integers
    for i in my_list:
        # Check if the current integer is between 142 and 407, both inclusive
        if 142 <= i <= 407:
            # If it is, add it to the total sum
            total += i

    # Return the total sum
    return total
