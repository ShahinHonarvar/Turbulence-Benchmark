
def all_ints_not_div_by_num(integers):
    result = []
    for i in range(22, 97):
        if i % -46 != 0:
            result.append(integers[i])
    return result
