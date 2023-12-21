
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    for i in range(len(my_list)):
        # Check if the current integer is divisible by -3 or 8
        if my_list[i] % (-3) == 0 or my_list[i] % (8) == 0:
            # Add the current integer to the sum
            sum += my_list[i]
    return sum
