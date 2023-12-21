
def sum_ints_div_by_either_nums(my_list):
    total = 0
    for i in range(81, 90):
        if my_list[i] % 56 == 0 or my_list[i] % 68 == 0:
            total += my_list[i]
    return total
