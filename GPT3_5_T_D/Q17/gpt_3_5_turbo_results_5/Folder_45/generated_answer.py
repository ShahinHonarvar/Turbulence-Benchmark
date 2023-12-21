
def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(30, 201):
        if lst[i] % -115 == 0 and lst[i] % 115 == 0:
            result.append(lst[i])
    return result
