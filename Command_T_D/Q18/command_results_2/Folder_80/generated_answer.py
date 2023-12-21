
def sum_ints_div_by_either_nums(lst):
    result = lst[14:93] + lst[14:93]
    result = [x for x in result if x % 71 == 0 or x % 81 == 0]
    return sum(result) if len(result) > 0 else 0
