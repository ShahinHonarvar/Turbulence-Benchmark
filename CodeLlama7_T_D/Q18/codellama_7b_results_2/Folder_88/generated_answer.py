
def sum_ints_div_by_either_nums(my_list):
    # Initialize sum to 0
    sum = 0
    # Loop through list and check if each integer is divisible by either 6 or 1
    for i in range(3, 10):
        if my_list[i] % 6 == 0 or my_list[i] % 1 == 0:
            sum += my_list[i]
    # Return sum
    return sum
