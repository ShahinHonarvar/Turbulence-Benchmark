
def sum_in_range(my_list):
    # Initialize the sum variable
    total = 0

    # Iterate through the list of integers
    for num in my_list:
        # Check if the current number is between 60 and 97, both inclusive
        if 60 <= num <= 97:
            # Add the current number to the total sum
            total += num

    # Return the total sum
    return total
