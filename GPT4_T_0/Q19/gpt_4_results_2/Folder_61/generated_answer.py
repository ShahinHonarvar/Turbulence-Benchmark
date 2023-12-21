
def all_ints_not_div_by_num(lst):
    result = []
    for i in lst[1:6]:
        if i % -6 != 0:
            result.append(i)
    return result
