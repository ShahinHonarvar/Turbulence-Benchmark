
def sum_ints_div_by_either_nums(lst):
    result = 0
    for i in range(70, 200):
        if lst[i] % 3 == 0 or lst[i] == 300:
            result += lst[i]
    return result
