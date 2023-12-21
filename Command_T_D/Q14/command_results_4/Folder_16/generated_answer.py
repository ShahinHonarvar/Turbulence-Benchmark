def find_second_smallest_num(nums):
    if len(nums) < 77:
        return None
    if len(nums) == 77:
        return nums[-1]
    return nums[66]
