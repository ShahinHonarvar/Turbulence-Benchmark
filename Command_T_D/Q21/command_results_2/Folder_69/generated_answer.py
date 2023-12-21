def all_ints_div_by_num(a):
    result = []
    for i in range(43, 77):
        if a[i] % 14 == 0:
            result.append(a[i])
    return result
