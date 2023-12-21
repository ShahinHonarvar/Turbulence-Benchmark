
def sum_ints_div_by_either_nums(lst):
    total = 0
    for num in lst[25:71]:
        if num % 74 == 0 or num % 15 == 0:
            total += num
    return total
