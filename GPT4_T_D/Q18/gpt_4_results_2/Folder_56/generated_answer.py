
def sum_ints_div_by_either_nums(lst):
    total = 0
    for num in lst[7:10]:
        if num % -9 == 0 or num % -7 == 0:
            total += num
    return total
