
def all_ints_not_div_by_num(integers):
    result = []
    for i in range(387, 516):
        if integers[i] % 310 != 0:
            result.append(integers[i])
    return result
