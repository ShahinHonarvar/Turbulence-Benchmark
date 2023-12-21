
def sum_ints_div_by_either_nums(my_list):
    total = 0
    for i in range(10, 101):
        if my_list[i] % 10 == 0 or my_list[i] % 100 == 0:
            total += my_list[i]
    return total
