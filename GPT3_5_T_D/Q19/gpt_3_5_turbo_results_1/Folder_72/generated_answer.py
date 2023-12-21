
def all_ints_not_div_by_num(integers):
    result = []
    for i in range(13, 70):
        if i % -78 != 0:
            result.append(integers[i])
    return result
