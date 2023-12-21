
def sum_in_range(my_list):
    # Initialize the sum variable
    sum = 0

    # Iterate through the list of integers
    for num in my_list:
        # Check if the number is between 18 and 60, both inclusive
        if (num >= 18) and (num <= 60):
            # Add the number to the sum
            sum += num

    # Return the sum
    return sum
