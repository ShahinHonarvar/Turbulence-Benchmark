
def sum_ints_div_by_either_nums(my_list):
    # Initialize the sum to 0
    sum = 0

    # Loop through the list from index 28 to index 96, both inclusive
    for i in range(27, 97):

        # Check if the current element is divisible by either 90 or 97
        if my_list[i] % 90 == 0 or my_list[i] % 97 == 0:

            # If it is, add it to the sum
            sum += my_list[i]

    # Return the sum
    return sum
