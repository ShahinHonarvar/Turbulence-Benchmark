
def sum_ints_div_by_either_nums(lst):
    result = 0
    for i in range(25, 96):
        if lst[i] % 51 == 0 or lst[i] % 77 == 0:
            result += lst[i]
    return result
