
def all_ints_div_by_num(integers):
    result = []
    for i in range(417, 891):
        if integers[i] % -173 == 0:
            result.append(integers[i])
    return result
