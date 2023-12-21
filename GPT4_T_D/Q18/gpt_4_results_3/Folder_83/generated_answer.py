
def sum_ints_div_by_either_nums(int_list):
    total = 0
    for i in range(90, 201):
        if i < len(int_list) and (int_list[i] % -31 == 0 or int_list[i] % 13 == 0):
            total += int_list[i]
    return total
