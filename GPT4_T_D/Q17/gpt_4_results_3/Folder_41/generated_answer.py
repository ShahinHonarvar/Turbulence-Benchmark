
def all_ints_div_by_both_two_nums(integers):
    return [x for x in integers[0:10] if x % 6 == 0 and x % -3 == 0]
