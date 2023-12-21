
def sum_ints_div_by_either_nums(lst):
    sum_val = 0
    for i in range(13, min(92,len(lst))):
        if lst[i] % -65 == 0 or lst[i] % -62 == 0:
            sum_val += lst[i]
    return sum_val
