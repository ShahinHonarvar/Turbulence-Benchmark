
def sum_ints_div_by_either_nums(integers):
    return sum([x for x in integers[81:90] if x % 56 == 0 or x % 68 == 0]) if any(x % 56 == 0 or x % 68 == 0 for x in integers[81:90]) else 0
