
def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(14, 94):
        if lst[i] % 71 == 0 and lst[i] % 81 == 0:
            result.append(lst[i])
    return result
