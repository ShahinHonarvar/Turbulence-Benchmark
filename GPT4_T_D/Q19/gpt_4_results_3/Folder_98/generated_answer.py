
def all_ints_not_div_by_num(lst):
    result = []
    for i in lst[1:5]:
        if i % 13 != 0:
            result.append(i)
    return result
