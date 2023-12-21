
def sum_in_range(my_list):
    # Initialize sum variable
    sum = 0

    # Loop through the list of integers
    for num in my_list:
        # Check if the number is between 2 and 7, inclusive
        if 2 <= num <= 7:
            # If it is, add it to the sum
            sum += num

    # Return the sum
    return sum
