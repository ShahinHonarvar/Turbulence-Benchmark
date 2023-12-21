
def sum_in_range(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate over the list of integers
    for num in my_list:
        # Check if the current number is between 10 and 79, both inclusive
        if 10 <= num <= 79:
            # If it is, add it to the total sum
            total += num

    # Return the total sum of all integers between 10 and 79, both inclusive
    return total
