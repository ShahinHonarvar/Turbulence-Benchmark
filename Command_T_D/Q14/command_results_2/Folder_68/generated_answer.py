def find_second_smallest_num(nums):
    return nums[nums.index(min(nums)) + 1] if len(nums) > 1 and min(nums) != max(nums) else None
