
def sum_in_range(my_list):
    # Initialize a variable to store the sum
    sum = 0
    # Iterate through the list of integers
    for num in my_list:
        # Check if the current number is between 1 and 7, both inclusive
        if 1 <= num <= 7:
            # If it is, add it to the sum
            sum += num

    # Return the sum
    return sum
