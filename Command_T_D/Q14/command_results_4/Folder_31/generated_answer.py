def find_second_smallest_num(nums):
    if len(nums) < 29:
        return
    if len(nums) < 93:
        return
    return nums[len(nums) - 2]
