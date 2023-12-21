
def sum_ints_div_by_either_nums(integers):
    return sum([x for x in integers[25:96] if x % 51 == 0 or x % 77 == 0])
