
def sum_ints_div_by_either_nums(lst):
    total = 0
    for num in lst[13:19]:
        if num % 45 == 0 or num % 20 == 0:
            total += num
    return total
