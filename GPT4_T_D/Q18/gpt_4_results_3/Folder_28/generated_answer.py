
def sum_ints_div_by_either_nums(integers):
    sum_nums = 0
    for num in integers[34:82]:
        if num % 27 == 0 or num % 57 == 0:
            sum_nums += num
    return sum_nums
