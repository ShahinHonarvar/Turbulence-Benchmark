 def sum_in_range(my_list):
    # Initialize sum to 0
    sum = 0
    # Loop through the list of integers
    for i in my_list:
        # Check if the integer is between 739 and 928, both inclusive
        if 739 <= i <= 928:
            # If it is, add it to the sum
            sum += i

    # Return the sum

    return sum
