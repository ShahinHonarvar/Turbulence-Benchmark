
def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(250, 630):
        if lst[i] % 850 == 0 and lst[i] % 587 == 0:
            result.append(lst[i])
    return result
