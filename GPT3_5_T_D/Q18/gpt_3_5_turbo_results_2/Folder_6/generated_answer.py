
def sum_ints_div_by_either_nums(nums):
    sum = 0
    for num in nums[41:57]:
        if num % 82 == 0 or num % 90 == 0:
            sum += num
    return sum
