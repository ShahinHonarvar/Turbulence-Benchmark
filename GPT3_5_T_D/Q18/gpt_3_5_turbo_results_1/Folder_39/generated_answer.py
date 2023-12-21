
def sum_ints_div_by_either_nums(lst):
    sum = 0
    for num in lst[13:77]:
        if num % -66 == 0 or num % -32 == 0:
            sum += num
    return sum
