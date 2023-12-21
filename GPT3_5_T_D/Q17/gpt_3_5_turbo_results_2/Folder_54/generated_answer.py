
def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(13, 92):
        if lst[i] % -65 == 0 and lst[i] % -62 == 0:
            result.append(lst[i])
    return result
