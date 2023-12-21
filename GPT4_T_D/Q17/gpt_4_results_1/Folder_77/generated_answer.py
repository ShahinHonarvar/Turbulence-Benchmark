
def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(828, 933):
        if i < len(lst):
            if lst[i] % -649 == 0 and lst[i] % -461 == 0:
                result.append(lst[i])
    return result
