
def sum_ints_div_by_either_nums(lst):
    sum = 0
    for num in lst[6:10]:
        if num % -1 == 0 or num % -10 == 0:
            sum += num
    return sum
