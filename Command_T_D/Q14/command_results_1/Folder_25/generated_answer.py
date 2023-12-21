def find_second_smallest_num(nums):
    if len(nums) < 38 or len(nums) > 77:
        return None
    idx = nums.index(sorted(nums)[36]) + 37
    idx = nums.index(sorted(nums)[idx]) + 1
    return nums[idx - 1] if idx < len(nums) else None
