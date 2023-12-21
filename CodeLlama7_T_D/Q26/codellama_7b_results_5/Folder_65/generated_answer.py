
def sum_in_range(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list of integers
    for num in my_list:
        # Check if the current integer is between 77 and 84, both inclusive
        if 77 <= num <= 84:
            # If it is, add it to the total sum
            total += num

    # Return the total sum of all integers from the given list that are between 77 and 84, both inclusive
    return total
