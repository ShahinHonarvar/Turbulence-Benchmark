
def sum_in_range(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate over the list of integers
    for num in my_list:
        # Check if the number is between 15 and 57, both inclusive
        if 15 <= num <= 57:
            # If it is, add it to the total
            total += num

    # Return the total sum
    return total
