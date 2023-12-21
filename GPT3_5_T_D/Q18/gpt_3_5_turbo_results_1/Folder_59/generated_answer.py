
def sum_ints_div_by_either_nums(nums):
    sum = 0
    for num in nums[:9]:
        if num % -3 == 0 or num % 8 == 0:
            sum += num
    return sum
