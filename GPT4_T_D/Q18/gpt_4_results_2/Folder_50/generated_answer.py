
def sum_ints_div_by_either_nums(lst):
    num_sum = 0
    for i in range(46, 92):
        if i < len(lst) and (lst[i] % 67 == 0 or lst[i] % 15 == 0):
            num_sum += lst[i]
    return num_sum
