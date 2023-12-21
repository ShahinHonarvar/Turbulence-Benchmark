
def all_ints_not_div_by_num(lst):
    indices = slice(24, 32)
    return [num for num in lst[indices] if num % 35 != 0]
