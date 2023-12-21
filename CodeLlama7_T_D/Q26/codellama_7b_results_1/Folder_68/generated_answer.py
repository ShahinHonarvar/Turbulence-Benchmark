 def sum_in_range(my_list):
    # Initialize a variable to store the sum
    total = 0
    # Loop through the given list of integers
    for num in my_list:
        # Check if the current integer is between 7 and 9, inclusive
        if 7 <= num <= 9:
            # If it is, add it to the sum
            total += num

    # Return the sum
    return total
