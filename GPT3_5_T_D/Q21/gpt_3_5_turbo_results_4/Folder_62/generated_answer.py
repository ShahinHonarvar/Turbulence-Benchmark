
def all_ints_div_by_num(integers):
    result = []
    for i in range(87, 90):
        if i < len(integers) and integers[i] % 55 == 0:
            result.append(integers[i])
    return result
