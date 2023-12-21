
def all_ints_div_by_both_two_nums(integers):
    result = []
    for i in range(80, 201):
        if i % 10 == 0 and i % 1000 == 0:
            result.append(integers[i])
    return result
