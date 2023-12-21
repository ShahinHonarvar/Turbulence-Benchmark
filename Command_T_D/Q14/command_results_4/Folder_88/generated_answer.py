def find_second_smallest_num(nums):
    if len(nums) < 6:
        return
    if len(nums) == 6:
        return nums[5]
    else:
        return nums[5] if nums[6] > nums[5] else nums[6]
