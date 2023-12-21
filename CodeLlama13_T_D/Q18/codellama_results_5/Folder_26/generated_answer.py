
def sum_ints_div_by_either_nums(my_list):
    total = 0
    for i in range(69, 71):
        if my_list[i] % 72 == 0 or my_list[i] % 70 == 0:
            total += my_list[i]
    return total
