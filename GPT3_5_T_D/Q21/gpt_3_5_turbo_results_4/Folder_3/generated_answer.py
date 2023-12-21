
def all_ints_div_by_num(lst):
    result = []
    for i in range(25, 60):
        if lst[i] % -26 == 0:
            result.append(lst[i])
    return result
