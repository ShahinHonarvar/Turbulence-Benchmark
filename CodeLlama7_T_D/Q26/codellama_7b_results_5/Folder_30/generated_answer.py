
def sum_in_range(my_list):
    # Initialize a variable to store the sum
    sum = 0

    # Iterate over the list of integers
    for num in my_list:
        # Check if the number is between 86 and 90, both inclusive
        if 86 <= num <= 90:
            # Add the number to the sum
            sum += num

    # Return the sum
    return sum
