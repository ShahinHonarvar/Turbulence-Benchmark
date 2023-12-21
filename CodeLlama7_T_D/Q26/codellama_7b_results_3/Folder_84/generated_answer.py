
def sum_in_range(my_list):
    # Initialize the sum variable
    sum = 0
    # Loop through the list of integers
    for num in my_list:
        # Check if the number is between 113 and 392, both inclusive
        if 113 <= num <= 392:
            # If it is, add it to the sum
            sum += num

    return sum
