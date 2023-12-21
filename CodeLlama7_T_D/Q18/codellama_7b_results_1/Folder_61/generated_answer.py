
def sum_ints_div_by_either_nums(my_list):
    total = 0
    for i in range(len(my_list))):
        if my_list[i] % -5 == 0 or my_list[i] % -6 == 0:
            total += my_list[i]
    return total
