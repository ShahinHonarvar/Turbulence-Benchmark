
def all_ints_div_by_num(lst):
    divisible_by_37 = [i for i in lst[29:52] if i % -37 == 0]
    return divisible_by_37
