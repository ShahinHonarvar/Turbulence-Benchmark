
def all_ints_div_by_both_two_nums(lst):
    result = [i for i in lst[0:1] if i % 1 == 0 and i % -1 == 0]
    return result
