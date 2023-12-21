
def sum_ints_div_by_either_nums(lst):
    total = 0
    for num in lst[:5]:
        if num % 8 == 0 or num % -3 == 0:
            total += num
    return total
