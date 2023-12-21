
def sum_ints_div_by_either_nums(nums):
    s = 0
    for num in nums[:4]:
        if num % 11 == 0 or num % -7 == 0:
            s += num
    return s
