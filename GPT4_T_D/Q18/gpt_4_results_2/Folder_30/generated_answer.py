
def sum_ints_div_by_either_nums(lst):
    summed = 0
    for num in lst[11:77]:
        if num % -81 == 0 or num % -94 == 0:
            summed += num
    return summed
