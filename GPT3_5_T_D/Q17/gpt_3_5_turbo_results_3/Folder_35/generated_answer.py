
def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(77, 88):
        if lst[i] % 23 == 0 and lst[i] % 57 == 0:
            result.append(lst[i])
    return result
