
def all_ints_not_div_by_num(integers):
    result = []
    for i in range(668, 739):
        if integers[i] % -172 != 0:
            result.append(integers[i])
    return result
