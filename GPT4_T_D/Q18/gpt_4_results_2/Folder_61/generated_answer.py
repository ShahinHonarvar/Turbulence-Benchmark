
def sum_ints_div_by_either_nums(lst):
    sum_nums = 0
    for i in range(min(len(lst), 7)):
        if lst[i] % -5 == 0 or lst[i] % -6 == 0:
            sum_nums += lst[i]
    return sum_nums
