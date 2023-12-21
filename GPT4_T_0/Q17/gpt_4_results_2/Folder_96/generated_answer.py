
def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(50, 201):
        if lst[i] % -34 == 0 and lst[i] % 64 == 0:
            result.append(lst[i])
    return result
