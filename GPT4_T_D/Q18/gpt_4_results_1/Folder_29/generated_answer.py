
def sum_ints_div_by_either_nums(lst):
    new_lst = lst[55:85]
    total = 0
    for num in new_lst:
        if num % -24 == 0 or num % -11 == 0:
            total += num
    return total
