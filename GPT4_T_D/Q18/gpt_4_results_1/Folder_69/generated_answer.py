
def sum_ints_div_by_either_nums(lst):
    total_sum = 0
    for i in range(61, 89):
        if i < len(lst) and (lst[i] % 31 == 0 or lst[i] % 11 == 0):
            total_sum += lst[i]
    return total_sum
