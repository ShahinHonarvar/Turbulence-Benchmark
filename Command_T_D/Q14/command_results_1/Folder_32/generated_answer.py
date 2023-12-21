def find_second_smallest_num(nums):
    return nums[nums.index(sorted(nums)[32]) - 1] if len(nums) > 32 else None
