
def sum_ints_div_by_either_nums(integers):
    return sum(x for x in integers[50:93] if x % -94 == 0 or x % -95 == 0)
