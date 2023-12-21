
def all_ints_div_by_both_two_nums(lst):
    res = [i for i in lst[10:101] if i % 10 == 0 and i % 100 == 0]
    return res
