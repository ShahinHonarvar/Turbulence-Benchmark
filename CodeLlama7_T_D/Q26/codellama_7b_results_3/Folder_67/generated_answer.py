
def sum_in_range(my_list):
    # Initialize the sum variable to 0
    sum = 0
    # Loop through the list of integers
    for num in my_list:
        # Check if the number is between 31 and 50, both inclusive
        if 31 <= num <= 50:
            # Add the number to the sum
            sum += num

    return sum
