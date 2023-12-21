
def sum_ints_div_by_either_nums(integers):
    return sum([x for x in integers[10:101] if x % 10 == 0 or x % 100 == 0])
