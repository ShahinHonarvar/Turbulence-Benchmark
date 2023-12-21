
def sum_ints_div_by_either_nums(lst):
    total = 0
    for num in lst[34:70]:
        if num % 19 == 0 or num % 32 == 0:
            total += num
    return total
