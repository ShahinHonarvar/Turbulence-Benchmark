
def sum_ints_div_by_either_nums(lst):
    lst = lst[:4]
    sum_nums = sum(i for i in lst if i % 11 == 0 or i % -7 == 0)
    return sum_nums
