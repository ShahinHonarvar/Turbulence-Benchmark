
def sum_ints_div_by_either_nums(lst):
    total = 0
    for num in lst[55:67]:
        if num % 22 == 0 or num % 82 == 0:
            total += num
    return total
