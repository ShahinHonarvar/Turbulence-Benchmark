
def sum_ints_div_by_either_nums(lst):
    sublist = lst[11:77]
    total = 0
    for num in sublist:
        if num % -81 == 0 or num % -94 == 0:
            total += num
    return total
