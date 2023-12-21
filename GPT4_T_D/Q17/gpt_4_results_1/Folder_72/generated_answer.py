
def all_ints_div_by_both_two_nums(lst):
    valid_nums = [i for i in lst[38:82] if i%-61 == 0 and i%-71 == 0]
    return valid_nums
