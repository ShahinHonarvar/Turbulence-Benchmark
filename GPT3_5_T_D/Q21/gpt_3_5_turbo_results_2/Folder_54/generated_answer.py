
def all_ints_div_by_num(lst):
    result = []
    for i in range(31, 73):
        if i >= len(lst):
            break
        if lst[i] % -63 == 0:
            result.append(lst[i])
    return result
