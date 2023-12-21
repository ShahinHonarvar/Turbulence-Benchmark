
def all_ints_div_by_num(integers):
    result = []
    for i in range(31, 93):
        if integers[i] % 20 == 0:
            result.append(integers[i])
    return result
