
def sum_ints_div_by_either_nums(nums):
    sum_nums = 0
    for num in nums[18:53]:
        if num % 15 == 0 or num % 57 == 0:
            sum_nums += num
    return sum_nums
