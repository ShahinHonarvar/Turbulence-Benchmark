
def sum_ints_div_by_either_nums(nums):
    sum = 0
    for num in nums[34:82]:
        if num % 27 == 0 or num % 57 == 0:
            sum += num
    return sum
