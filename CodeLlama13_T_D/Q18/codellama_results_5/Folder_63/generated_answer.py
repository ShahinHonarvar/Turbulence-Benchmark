
def sum_ints_div_by_either_nums(my_list):
    total = 0
    for i in range(31, 51):
        if my_list[i] % 81 == 0 or my_list[i] % 64 == 0:
            total += my_list[i]
    return total
