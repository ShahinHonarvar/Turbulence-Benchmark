
def all_ints_div_by_num(integers):
    result = []
    for i in range(52, 73):
        if integers[i] % -15 == 0:
            result.append(integers[i])
    return result
