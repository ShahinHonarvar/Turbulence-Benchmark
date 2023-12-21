
def sum_ints_div_by_either_nums(lst):
    sum_div = 0
    for num in lst[86:90]:
        if num % -61 == 0 or num % -79 == 0:
            sum_div += num
    if sum_div == 0:
        return 0
    else:
        return sum_div
