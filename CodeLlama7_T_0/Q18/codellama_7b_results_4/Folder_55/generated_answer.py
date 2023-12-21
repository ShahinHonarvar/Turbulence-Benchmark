
def sum_ints_div_by_either_nums(my_list):
    # Initialize the sum to 0
    total = 0

    # Loop through the first 10 elements of the list
    for i in range(10):

        # Check if the current element is divisible by either 10 or 100
        if my_list[i] % 10 == 0 or my_list[i] % 100 == 0:

            # If it is, add it to the total
            total += my_list[i]

    # Return the sum
    return total
