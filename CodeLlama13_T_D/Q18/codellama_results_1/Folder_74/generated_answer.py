
def sum_ints_div_by_either_nums(my_list):
    total = 0
    for i in range(90, 98):
        if my_list[i] % 13 == 0 or my_list[i] % 35 == 0:
            total += my_list[i]
    return total
