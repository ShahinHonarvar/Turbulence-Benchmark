
def all_ints_div_by_both_two_nums(list):
    result = []
    for i in range(0, len(list)):
        if list[i] % 2 == 0 and list[i] % 1 == 0:
            result.append(list[i])
    return result
