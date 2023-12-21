
def sum_ints_div_by_either_nums(lst):
    sums = 0
    for num in lst[42:44]:
        if num % 15 == 0 or num % 87 == 0:
            sums += num
    return sums
