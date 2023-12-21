
def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(90,201):
        if lst[i] % -31 == 0 and lst[i] % 13 == 0:
            result.append(lst[i])
    return result
