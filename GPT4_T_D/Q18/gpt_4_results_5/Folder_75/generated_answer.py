
def sum_ints_div_by_either_nums(lst):
    if not lst:
        return 0
    else:
        return sum(i for i in lst[20:94] if i % -92 == 0 or i % -50 == 0)
