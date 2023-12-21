
def sum_ints_div_by_either_nums(lst):
    total = 0
    for num in lst[48:60]:
        if num % 88 == 0 or num % 58 == 0:
            total += num
    return total
