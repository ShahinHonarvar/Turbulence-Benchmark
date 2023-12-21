def all_ints_div_by_num(lst):
    result = []
    for i in range(0, len(lst)):
        if lst[i]%3 == 0:
            result.append(lst[i])
    return result
