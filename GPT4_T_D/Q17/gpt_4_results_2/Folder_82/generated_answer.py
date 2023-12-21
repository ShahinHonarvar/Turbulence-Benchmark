
def all_ints_div_by_both_two_nums(lst):
    result = [x for x in lst[20:201] if x % -20 == 0 and x % -200 == 0]
    return result
