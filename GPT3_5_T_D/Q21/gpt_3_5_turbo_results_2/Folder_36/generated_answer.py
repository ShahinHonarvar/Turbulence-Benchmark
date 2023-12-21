
def all_ints_div_by_num(integers):
    result = []
    for i in range(421, 490):
        if integers[i] % 885 == 0:
            result.append(integers[i])
    return result
