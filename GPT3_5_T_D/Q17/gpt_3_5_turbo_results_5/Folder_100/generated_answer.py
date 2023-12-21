
def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(72, 94):
        if lst[i] % 32 == 0 and lst[i] % 44 == 0:
            result.append(lst[i])
    return result
