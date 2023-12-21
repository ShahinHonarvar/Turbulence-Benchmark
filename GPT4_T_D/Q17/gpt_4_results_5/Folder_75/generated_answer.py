
def all_ints_div_by_both_two_nums(lst):
    result = [i for i in lst[20:94] if i % -92 == 0 and i % -50 == 0]
    return result
