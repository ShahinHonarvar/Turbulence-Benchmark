
def sum_in_range(my_list):
    # Initialize sum to 0
    sum = 0
    # Iterate through the list of integers
    for num in my_list:
        # Check if the number is between 20 and 93, both inclusive
        if 20 <= num <= 93:
            # Add the number to the sum
            sum += num

    return sum
