
def sum_in_range(my_list):
    # Initialize the sum variable
    sum = 0

    # Loop through the list of integers
    for i in my_list:
        # Check if the current integer is between 60 and 90, both inclusive
        if 60 <= i <= 90:
            # If it is, add it to the sum
            sum += i

    # Return the sum
    return sum
