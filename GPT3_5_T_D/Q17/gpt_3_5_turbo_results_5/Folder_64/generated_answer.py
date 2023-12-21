
def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(4):
        if lst[i] % 11 == 0 and lst[i] % -7 == 0:
            result.append(lst[i])
    return result
