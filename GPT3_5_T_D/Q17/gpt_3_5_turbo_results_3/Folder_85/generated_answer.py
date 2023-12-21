
def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(1, 9):
        if lst[i] % -9 == 0 and lst[i] % -3 == 0:
            result.append(lst[i])
    return result
