
def all_ints_not_div_by_num(lst):
    results = []
    for i in lst[2:]:
        if i % lst[0] != 0 and i % lst[1] != 0:
            results.append(i)
    return results
