
def all_ints_div_by_num(lst):
    result = []
    for i in range(57, 68):
        if lst[i] % 90 == 0:
            result.append(lst[i])
    return result
