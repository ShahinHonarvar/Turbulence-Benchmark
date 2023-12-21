
def all_ints_div_by_both_two_nums(list):
    result = []
    for i in range(13, 91):
        if list[i] % -65 == 0 and list[i] % -62 == 0:
            result.append(list[i])
    return result
