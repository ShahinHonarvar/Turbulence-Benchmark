def find_second_smallest_num(nums):
    return nums[nums.index(sorted(nums)[-2]) - 1] if len(nums) > 51 and nums[51] < nums[52] else None
