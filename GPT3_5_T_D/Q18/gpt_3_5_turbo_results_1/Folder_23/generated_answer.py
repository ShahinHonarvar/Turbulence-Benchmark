
def sum_ints_div_by_either_nums(lst):
    total = 0
    for num in lst[69:98]:
        if num % -90 == 0 or num % -67 == 0:
            total += num
    return total
