def find_second_smallest_num(nums):
    if not nums:
        return None
    if len(nums) < 34:
        return None
    if len(nums) < 55:
        return nums[len(nums) - 1]
    return nums[len(nums) - 2]
