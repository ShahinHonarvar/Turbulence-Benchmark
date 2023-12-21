
def sum_ints_div_by_either_nums(nums):
    return sum(num for num in nums[0:1] if num % 1 == 0 or num % -1 == 0)
