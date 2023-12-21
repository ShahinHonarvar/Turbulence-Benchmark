
def sum_in_range(my_list):
    # Initialize a variable to store the sum
    sum = 0
    # Loop through the list of integers
    for num in my_list:
        # Check if the current integer is between 60 and 97, both inclusive
        if (num >= 60) and (num <= 97):
            # If it is, add it to the sum
            sum += num

    # Return the sum
    return sum
