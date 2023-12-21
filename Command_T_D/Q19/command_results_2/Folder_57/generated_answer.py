def all_ints_not_div_by_num(lst):
    result = []
    for n in range(56, 88):
        if n % -59 != 0:
            result.append(n)
    return result
