
def all_ints_div_by_both_two_nums(lst):
    res = [i for i in lst[240:902] if i % 546 == 0 and i % 709 == 0]
    return res
