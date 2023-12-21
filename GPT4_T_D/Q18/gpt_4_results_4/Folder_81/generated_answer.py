
def sum_ints_div_by_either_nums(lst):
    total = 0
    for num in lst[10:101]:
        if num % 10 == 0 or num % 100 == 0:
            total += num
    return total
