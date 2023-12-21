
def if_perfect_num(nums):
    if len(nums) >= 42 and sum(divisor for divisor in range(1, nums[41]) if nums[41] % divisor == 0) == nums[41]:
        return True
    return False
