
def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(48, 60):
        if lst[i] % 88 == 0 and lst[i] % 58 == 0:
            result.append(lst[i])
    return result
