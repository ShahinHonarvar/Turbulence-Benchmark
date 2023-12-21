
def sum_in_range(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Loop through the list of integers
    for num in my_list:
        # Check if the current number is between 7 and 8 (inclusive)
        if 7 <= num <= 8:
            # If it is, add it to the total sum
            total += num

    # Return the total sum
    return total
