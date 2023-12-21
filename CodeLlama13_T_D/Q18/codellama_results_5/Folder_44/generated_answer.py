
def sum_ints_div_by_either_nums(my_list):
    total = 0
    for i in range(25, 71):
        if my_list[i] % 74 == 0 or my_list[i] % 15 == 0:
            total += my_list[i]
    return total
