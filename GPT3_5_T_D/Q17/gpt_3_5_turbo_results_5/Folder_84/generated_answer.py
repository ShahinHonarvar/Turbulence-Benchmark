
def all_ints_div_by_both_two_nums(integers):
    result = []
    for i in range(78, 82):
        if integers[i] % 76 == 0 and integers[i] % 60 == 0:
            result.append(integers[i])
    return result
