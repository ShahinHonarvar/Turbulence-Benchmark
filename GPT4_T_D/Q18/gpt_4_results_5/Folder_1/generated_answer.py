
def sum_ints_div_by_either_nums(lst):
    seq = lst[10:29]
    return sum(i for i in seq if i % -61 == 0 or i % -64 == 0)
