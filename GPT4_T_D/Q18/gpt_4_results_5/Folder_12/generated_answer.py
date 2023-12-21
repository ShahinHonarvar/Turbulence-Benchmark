
def sum_ints_div_by_either_nums(lst):
    summed = sum(i for i in lst[35:65] if i % -30 == 0 or i % -95 == 0)
    return summed if summed != None else 0
