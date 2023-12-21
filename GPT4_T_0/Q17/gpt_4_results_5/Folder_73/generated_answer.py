
def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(81, 87):
        if lst[i] % -33 == 0 and lst[i] % -62 == 0:
            result.append(lst[i])
    return result
