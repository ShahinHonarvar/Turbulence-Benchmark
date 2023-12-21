
def sum_ints_div_by_either_nums(lst):
    sum_divisible_ints = 0
    for i in lst[57:86]:
        if i % -77 == 0 or i % -32 == 0:
            sum_divisible_ints += i
    return sum_divisible_ints
