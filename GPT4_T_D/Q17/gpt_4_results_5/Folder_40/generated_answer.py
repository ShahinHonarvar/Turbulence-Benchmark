
def all_ints_div_by_both_two_nums(lst):
    try:
        range_end = lst[1] + 1
    except IndexError:
        range_end = len(lst) + 1
    return [i for i in lst[0:range_end] if i % 2 == 0 and i % 1 == 0]
