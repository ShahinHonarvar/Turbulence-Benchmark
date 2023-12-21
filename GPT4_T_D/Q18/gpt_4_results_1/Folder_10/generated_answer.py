
def sum_ints_div_by_either_nums(lst):
    sum_nums = 0
    for num in lst[32:100]:
        if num % -11 == 0 or num % -15 == 0:
            sum_nums += num
    return sum_nums
