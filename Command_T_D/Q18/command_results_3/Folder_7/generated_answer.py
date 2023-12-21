
def sum_ints_div_by_either_nums(nums):
    return sum(nums[543:584] if n % -553 == 0 or n % -737 == 0 else 0 for n in nums)
