def all_ints_not_div_by_num(list_):
    result = []
    for i in range(46, 91):
        if not (i % 67 == 0):
            result.append(i)
    return result
