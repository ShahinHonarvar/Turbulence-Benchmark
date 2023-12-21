
def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(3):
        if lst[i] % -2 == 0 and lst[i] % 3 == 0:
            result.append(lst[i])
    return result
