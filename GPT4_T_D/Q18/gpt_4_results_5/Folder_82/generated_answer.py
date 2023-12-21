
def sum_ints_div_by_either_nums(lst):
    sum_nums = 0
    for num in lst[20:201]:
        if num % -20 == 0 or num % -200 == 0:
            sum_nums += num
    return sum_nums
