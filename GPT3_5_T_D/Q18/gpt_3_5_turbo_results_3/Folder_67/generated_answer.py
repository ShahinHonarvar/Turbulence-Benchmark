
def sum_ints_div_by_either_nums(lst):
    sum = 0
    for i in range(24, 33):
        if lst[i] % 35 == 0 or lst[i] % 87 == 0:
            sum += lst[i]
    return sum
