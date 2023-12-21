
def sum_in_range(my_list):
    # Initialize a variable to store the sum
    total = 0
    # Loop through the list of integers
    for num in my_list:
        # Check if the number is between 46 and 91, both inclusive
        if 46 <= num <= 91:
            # If it is, add it to the total sum
            total += num

    # Return the total sum
    return total
