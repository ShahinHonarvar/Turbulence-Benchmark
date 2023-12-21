
def sum_in_range(my_list):
    # Initialize the sum to 0
    total = 0
    # Loop through the list of integers
    for num in my_list:
        # Check if the number is between 56 and 90 (both inclusive)
        if 56 <= num <= 90:
            # If it is, add it to the total sum
            total += num

    # Return the total sum

    return total
