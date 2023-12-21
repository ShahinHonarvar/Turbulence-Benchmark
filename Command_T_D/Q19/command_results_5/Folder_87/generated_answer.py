def all_ints_not_div_by_num(lst):
    result = []
    for i in range(19, 69):
        if not lst[i] % 97:
            break
        result.append(lst[i])
    return result
