
def all_ints_not_div_by_num(integers):
    result = []
    for i in range(60, 200):
        if i % 9 != 0:
            result.append(integers[i])
    return result
