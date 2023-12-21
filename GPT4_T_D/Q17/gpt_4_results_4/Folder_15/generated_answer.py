
def all_ints_div_by_both_two_nums(lst):
    result = [i for i in lst[:3] if i % -2 == 0 and i % 3 == 0]
    return result
