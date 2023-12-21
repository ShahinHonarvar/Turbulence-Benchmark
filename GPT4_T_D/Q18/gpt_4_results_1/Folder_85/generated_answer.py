
def sum_ints_div_by_either_nums(lst):
    sum_div = sum(i for i in lst[1:9] if i % -9 == 0 or i % -3 == 0)
    return sum_div if sum_div else 0
