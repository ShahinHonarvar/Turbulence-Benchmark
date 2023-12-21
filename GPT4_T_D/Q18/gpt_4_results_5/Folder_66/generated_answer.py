
def sum_ints_div_by_either_nums(lst):
    sum_of_nums = 0
    for num in lst[58:82]:
        if num % 55 == 0 or num % 10 == 0:
            sum_of_nums += num
    return sum_of_nums
