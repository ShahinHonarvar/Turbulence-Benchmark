
def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(11, 77):
        if lst[i] % -81 == 0 and lst[i] % -94 == 0:
            result.append(lst[i])
    return result
