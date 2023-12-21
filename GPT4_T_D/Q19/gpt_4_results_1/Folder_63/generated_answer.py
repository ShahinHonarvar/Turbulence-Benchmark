
def all_ints_not_div_by_num(l):
    result = []
    for i in range(21, 43):
        if l[i] % 95 != 0:
            result.append(l[i])
    return result
