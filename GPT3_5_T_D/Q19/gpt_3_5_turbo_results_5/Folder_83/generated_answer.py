
def all_ints_not_div_by_num(lst):
    result = []
    for i in range(90, 200):
        if i % -31 != 0:
            result.append(lst[i])
    return result
