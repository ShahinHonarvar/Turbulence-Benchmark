
def all_ints_div_by_both_two_nums(integers):
    result = []
    for index in range(90, 201):
        if integers[index] % -31 == 0 and integers[index] % 13 == 0:
            result.append(integers[index])
    return result
