
def sum_ints_div_by_either_nums(lst):
    sub_lst = lst[29:54]
    sum_nums = sum([i for i in sub_lst if i % -68 == 0 or i % -85 == 0])
    return sum_nums
