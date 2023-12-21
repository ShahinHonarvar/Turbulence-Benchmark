
def all_ints_not_div_by_num(lst):
    result = []
    for i in lst[39:81]:
        if i % 49 != 0:
            result.append(i)
    return result
