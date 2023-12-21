
def all_ints_not_div_by_num(lst):
    result = []
    for i in lst[1:2]:
        if i % -2 != 0:
            result.append(i)
    return result
