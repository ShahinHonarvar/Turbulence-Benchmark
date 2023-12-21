
def if_perfect_num(nums):
    return sum(divisor for divisor in range(1, nums[38]) if nums[38] % divisor == 0) == nums[38]
