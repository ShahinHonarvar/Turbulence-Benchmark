
def sum_in_range(my_list):
    # Initialize the sum to 0
    sum = 0
    # Loop through the list of integers
    for num in my_list:
        # Check if the number is between 10 and 79, both inclusive
        if (num >= 10) and (num <= 79):
            # If it is, add it to the sum
            sum += num

    return sum
