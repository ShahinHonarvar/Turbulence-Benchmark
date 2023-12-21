
def sum_ints_div_by_either_nums(lst):
    result = 0
    for i in range(61, 89):
        if lst[i] % 31 == 0 or lst[i] % 11 == 0:
            result += lst[i]
    return result
