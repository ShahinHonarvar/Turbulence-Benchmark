def if_perfect_num(nums):
    return (len(nums) == len(set(nums)) and len(nums) == len(nums) * 2 and nums[37] == sum(nums) == len(nums))
