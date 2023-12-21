
def sum_ints_div_by_either_nums(my_list):
    # Initialize the sum to 0
    sum = 0

    # Loop through the list from index 55 to index 84, both inclusive
    for i in range(55, 85):

        # Check if the current element is divisible by either -24 or -11
        if my_list[i] % (-24) == 0 or my_list[i] % (-11) == 0:

            # If it is, add it to the sum
            sum += my_list[i]

    # Return the sum
    return sum
