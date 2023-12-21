
def sum_in_range(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Loop through the list of integers
    for num in my_list:
        # Check if the number is between -885 and -817, both inclusive
        if -885 <= num <= -817:
            # If it is, add it to the total
            total += num

    # Return the sum of all integers from the given list that are between -885 and -817, both inclusive
    return total
