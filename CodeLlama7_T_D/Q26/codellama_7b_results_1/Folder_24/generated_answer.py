
def sum_in_range(my_list):
    # Initialize the sum to 0
    sum = 0
    # Iterate over the list of integers
    for num in my_list:
        # Check if the number is between -91 and -41, both inclusive
        if -91 <= num <= -41:
            # If it is, add it to the sum
            sum += num

    # Return the sum
    return sum
