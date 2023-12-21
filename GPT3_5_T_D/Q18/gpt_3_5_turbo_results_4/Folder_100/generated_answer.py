
def sum_ints_div_by_either_nums(lst):
    sum = 0
    for i in range(72, 94):
        if lst[i] % 32 == 0 or lst[i] % 44 == 0:
            sum += lst[i]
    return sum
