
def sum_in_range(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Loop through each integer in the list
    for num in my_list:
        # Check if the integer is between 5 and 8, inclusive
        if 5 <= num <= 8:
            # If it is, add it to the sum
            total += num

    # Return the sum
    return total
