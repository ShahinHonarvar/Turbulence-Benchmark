
def all_ints_div_by_both_two_nums(lst):
    if 7 <= len(lst) <= 9:
        return [x for x in lst[7:10] if x % 2 == 0 and x % 3 == 0]
    else:
        return []
