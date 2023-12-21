
def all_ints_div_by_both_two_nums(lst):
    result = [i for i in lst[90:201] if i % -31 == 0 and i % 13 == 0]
    return result
