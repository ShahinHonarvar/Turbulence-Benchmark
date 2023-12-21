def find_second_smallest_num(nums):
    if len(nums) < 6:
        return None
    idx = nums.index(sorted(nums)[0])
    return nums[idx + 1] if idx + 1 < len(nums) else None
