
def sum_ints_div_by_either_nums(lst):
    result = 0
    for i in range(58, 81 + 1):
        if lst[i] % 55 == 0 or lst[i] % 10 == 0:
            result += lst[i]
    return result
