
def sum_ints_div_by_either_nums(lst):
    result = 0
    for i in range(57, 85):
        if lst[i] % -30 == 0 or lst[i] % -88 == 0:
            result += lst[i]
    return result
