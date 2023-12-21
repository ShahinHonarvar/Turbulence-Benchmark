
def sum_ints_div_by_either_nums(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Loop through the list from index 25 to index 95, both inclusive
    for i in range(25, 96):

        # Check if the current element is divisible by either 51 or 77
        if my_list[i] % 51 == 0 or my_list[i] % 77 == 0:

            # If it is, add it to the total sum
            total += my_list[i]

    # Return the total sum
    return total
