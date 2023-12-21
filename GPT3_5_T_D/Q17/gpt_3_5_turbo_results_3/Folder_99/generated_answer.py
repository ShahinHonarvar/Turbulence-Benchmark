
def all_ints_div_by_both_two_nums(integers):
    result = []
    for i in range(154, 799):
        if integers[i] % 275 == 0 and integers[i] % 580 == 0:
            result.append(integers[i])
    return result
