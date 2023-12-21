
def all_ints_not_div_by_num(lst):
    result = []
    for i in range(91, 97):
        if lst[i] % 13 != 0:
            result.append(lst[i])
    return result
