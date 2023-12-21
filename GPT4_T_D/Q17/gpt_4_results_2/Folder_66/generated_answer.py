
def all_ints_div_by_both_two_nums(ints):
    result = []
    for i in range(58, 82):
        if i < len(ints):
            if ints[i] % 55 == 0 and ints[i] % 10 == 0:
                result.append(ints[i])
    return result
