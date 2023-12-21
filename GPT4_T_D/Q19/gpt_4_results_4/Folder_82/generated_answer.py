
def all_ints_not_div_by_num(lst):
    result = []
    for i in lst[21:200]:
        if i % -200 != 0:
            result.append(i)
    return result
