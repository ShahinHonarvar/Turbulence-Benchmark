
def sum_ints_div_by_either_nums(lst):
    result = 0
    for i in range(len(lst)):
        if lst[i] % 4 == 0 or lst[i] % 6 == 0:
            result += lst[i]
    return result
