
def sum_ints_div_by_either_nums(integers):
    nums_sum = 0
    for num in integers[34:82]:
        if num % 27 == 0 or num % 57 == 0:
            nums_sum += num
    return nums_sum
