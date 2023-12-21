
def sum_in_range(my_list):
    # Initialize a variable to store the sum
    sum = 0
    # Iterate through the list of integers
    for num in my_list:
        # Check if the current integer is between 4 and 5, both inclusive
        if 4 <= num <= 5:
            # If it is, add it to the sum
            sum += num

    # Return the sum
    return sum
