
def sum_ints_div_by_either_nums(int_list):
    total = 0
    for i in range(1, 8):
        if int_list[i] % -9 == 0 or int_list[i] % -3 == 0:
            total += int_list[i]
    return total
