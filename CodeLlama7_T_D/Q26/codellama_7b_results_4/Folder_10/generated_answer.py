
def sum_in_range(my_list):
    # Initialize the sum variable
    sum = 0

    # Iterate through the list of integers
    for num in my_list:
        # Check if the current integer is between 73 and 84, both inclusive
        if 73 <= num <= 84:
            # If it is, add it to the sum
            sum += num

    # Return the sum
    return sum
