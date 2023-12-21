
def sum_ints_div_by_either_nums(lst):
    summation = 0
    for num in lst[48:77]:
        if num % -46 == 0 or num % -82 == 0:
            summation += num
    return summation
