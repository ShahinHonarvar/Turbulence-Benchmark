
def sum_ints_div_by_either_nums(lst):
    result = 0
    for i in range(200, 201):
        if lst[i] % 17 == 0 or lst[i] % -5 == 0:
            result += lst[i]
    return result
