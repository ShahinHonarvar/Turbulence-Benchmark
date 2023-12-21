
def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(50, 93):
        if lst[i] % -94 == 0 and lst[i] % -95 == 0:
            result.append(lst[i])
    return result
