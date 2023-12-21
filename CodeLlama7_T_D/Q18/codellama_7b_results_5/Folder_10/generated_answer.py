
def sum_ints_div_by_either_nums(my_list):
    # Initialize the sum to 0
    sum = 0
    # Loop through the list from index 32 to index 99
    for i in range(32, 100):
        # Check if the current element is divisible by either -11 or -15
        if my_list[i] % (-11) == 0 or my_list[i] % (-15) == 0:
            # If it is, add it to the sum
            sum += my_list[i]
    return sum
