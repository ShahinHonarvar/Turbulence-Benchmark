
def all_ints_div_by_num(lst):
    result = []
    for i in range(11, 110 + 1):
        if i % 11 == 0 and i in lst:
            result.append(i)
    return result
