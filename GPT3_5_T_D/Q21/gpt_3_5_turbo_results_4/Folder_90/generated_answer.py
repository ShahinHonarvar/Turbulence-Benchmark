
def all_ints_div_by_num(lst):
    result = []
    for i in range(417, 891):
        if lst[i] % -173 == 0:
            result.append(lst[i])
    return result
