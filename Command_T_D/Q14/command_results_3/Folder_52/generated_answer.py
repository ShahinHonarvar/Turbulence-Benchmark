def find_second_smallest_num(nums):
    idx = nums.index(sorted(nums)[63])
    return nums[idx + 1] if idx + 1 < len(nums) - 1 else None
