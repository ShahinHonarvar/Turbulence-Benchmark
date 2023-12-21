
def sum_ints_div_by_either_nums(lst):
    result = 0
    for i in range(34, min(70, len(lst))):
        if lst[i] % 19 == 0 or lst[i] % 32 == 0:
            result += lst[i]
    return result
