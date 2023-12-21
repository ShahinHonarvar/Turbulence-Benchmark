
def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(154, 799):
        if lst[i] % 275 == 0 and lst[i] % 580 == 0:
            result.append(lst[i])
    return result
