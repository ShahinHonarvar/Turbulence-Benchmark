
def sum_ints_div_by_either_nums(my_list):
    total = 0
    for i in range(80, 201):
        if my_list[i] % 10 == 0 or my_list[i] % 1000 == 0:
            total += my_list[i]
    return total
