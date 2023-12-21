
def all_ints_div_by_num(lst):
    result = []
    for i in range(601, 699):
        if lst[i] % 901 == 0:
            result.append(lst[i])
    return result
