
def sum_in_range(my_list):
    # Initialize the sum to 0
    sum = 0
    # Loop through each integer in the list
    for num in my_list:
        # Check if the number is between 10 and 97, inclusive
        if 10 <= num <= 97:
            # Add the number to the sum
            sum += num

    # Return the sum
    return sum
