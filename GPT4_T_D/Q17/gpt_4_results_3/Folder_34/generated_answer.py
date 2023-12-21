
def all_ints_div_by_both_two_nums(lst):
    result = [i for i in lst[60:201] if i % 9 == 0 and i % 11 == 0]
    return result
