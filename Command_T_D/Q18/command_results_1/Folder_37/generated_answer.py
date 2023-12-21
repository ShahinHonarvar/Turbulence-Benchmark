
def sum_ints_div_by_either_nums(nums):
    return sum(nums[2:-2] if num in nums[2:-2] and num % -1 == 0 or num % -7 == 0 else 0 for num in nums)
