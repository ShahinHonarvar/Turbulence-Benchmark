
def all_ints_not_div_by_num(lst):
    result = []
    for i in lst[2:]:
        if i % -1 != 0:
            result.append(i)
    return result
