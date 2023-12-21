
def all_ints_div_by_both_two_nums(integers):
    result = []
    for i in range(28, 97+1):
        if integers[i] % 90 == 0 and integers[i] % 97 == 0:
            result.append(integers[i])
    return result
