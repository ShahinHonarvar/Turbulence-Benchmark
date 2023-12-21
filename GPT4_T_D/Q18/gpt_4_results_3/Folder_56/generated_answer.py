
def sum_ints_div_by_either_nums(lst):
    sum_lst = 0
    for index in range(7, 10):
        if lst[index] % (-9) == 0 or lst[index] % (-7) == 0:
            sum_lst += lst[index]
    return sum_lst
