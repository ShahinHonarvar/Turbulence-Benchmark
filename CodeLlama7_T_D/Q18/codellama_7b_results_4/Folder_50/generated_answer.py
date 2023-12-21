
def sum_ints_div_by_either_nums(my_list):
    # Initialize the sum to 0
    total = 0

    # Iterate through the list from index 46 to index 91, both inclusive
    for i in range(46, 92):

        # Check if the current element is divisible by either 67 or 15
        if my_list[i] % 67 == 0 or my_list[i] % 15 == 0:

            # If it is, add it to the total sum
            total += my_list[i]

    # Return the total sum
    return total
