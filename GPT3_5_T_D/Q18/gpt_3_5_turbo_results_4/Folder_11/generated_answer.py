
def sum_ints_div_by_either_nums(lst):
    sum = 0
    for i in range(22, 25):
        if lst[i] % -85 == 0 or lst[i] % -30 == 0:
            sum += lst[i]
    return sum
