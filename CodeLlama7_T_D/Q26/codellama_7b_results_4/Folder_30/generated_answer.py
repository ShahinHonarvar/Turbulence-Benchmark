
def sum_in_range(my_list):
    # Initialize a variable to store the sum
    total = 0
    # Iterate over the list of integers
    for num in my_list:
        # Check if the current number is between 86 and 90, both inclusive
        if 86 <= num <= 90:
            # If it is, add it to the total sum
            total += num

    # Return the total sum of all integers between 86 and 90, both inclusive
    return total
