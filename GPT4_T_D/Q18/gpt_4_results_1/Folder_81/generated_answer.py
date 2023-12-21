
def sum_ints_div_by_either_nums(lst):
    if len(lst)<101:
        range_lst = lst[10:]
    else:
        range_lst = lst[10:101]
    return sum(num for num in range_lst if num % 10 == 0 or num % 100 == 0)
