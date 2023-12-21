
def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(73, 87):
        if lst[i] % 54 == 0 and lst[i] % 82 == 0:
            result.append(lst[i])
    return result
