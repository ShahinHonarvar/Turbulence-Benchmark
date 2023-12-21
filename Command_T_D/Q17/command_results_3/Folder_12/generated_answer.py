
def all_ints_div_by_both_two_nums(lst):
    return [x for x in range(35, 65) if (x // -30) % -95 == 0 and x % -30 == 0 and x % -95 == 0]
