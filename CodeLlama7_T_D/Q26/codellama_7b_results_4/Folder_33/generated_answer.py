
def sum_in_range(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Loop through the list of integers
    for num in my_list:
        # Check if the number is between 368 and 679, both inclusive
        if 368 <= num <= 679:
            # If it is, add it to the total sum
            total += num

    # Return the total sum
    return total
