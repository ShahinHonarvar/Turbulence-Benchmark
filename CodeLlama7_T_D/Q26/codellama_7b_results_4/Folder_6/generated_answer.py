
def sum_in_range(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate over the list of integers
    for num in my_list:
        # Check if the current integer is between 335 and 611, both inclusive
        if 335 <= num <= 611:
            # If it is, add it to the total sum
            total += num

    # Return the total sum
    return total
