
def sum_ints_div_by_either_nums(lst):
    total = 0
    for num in lst[32:100]:
        if num % -11 == 0 or num % -15 == 0:
            total += num
    return total
