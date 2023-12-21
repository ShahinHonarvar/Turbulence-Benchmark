
def all_ints_div_by_num(lst):
    result = []
    for i in range(255, 619):
        if lst[i] % 965 == 0:
            result.append(lst[i])
    return result
