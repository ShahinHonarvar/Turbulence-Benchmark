
def sum_ints_div_by_either_nums(my_list):
    # Initialize the sum to 0
    sum = 0

    # Loop through the list from index 7 to index 9, both inclusive
    for i in range(7, 10):

        # If the current element is divisible by either 2 or 3, add it to the sum
        if my_list[i] % 2 == 0 or my_list[i] % 3 == 0:
            sum += my_list[i]

    # Return the sum
    return sum
