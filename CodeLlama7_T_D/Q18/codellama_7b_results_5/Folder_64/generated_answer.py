
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    nums_to_check = [11, -7]
    # Iterate over the list and check if each integer is divisible by either 11 or -7
    for i in range(4):
        if my_list[i] % nums_to_check[0] == 0 or my_list[i] % nums_to_check[1] == 0:
            sum += my_list[i]
    return sum
