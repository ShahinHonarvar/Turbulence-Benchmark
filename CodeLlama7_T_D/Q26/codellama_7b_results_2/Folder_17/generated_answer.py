
def sum_in_range(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate over the list of integers
    for num in my_list:
        # Check if the current integer is between -816 and -166, both inclusive
        if -816 <= num <= -166:
            # If it is, add it to the sum
            total += num

    # Return the sum
    return total
