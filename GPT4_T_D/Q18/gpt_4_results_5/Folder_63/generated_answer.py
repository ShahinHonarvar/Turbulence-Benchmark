
def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(31, 51):
        if i < len(lst) and (lst[i] % 81 == 0 or lst[i] % 64 == 0): 
            total += lst[i]
    return total
