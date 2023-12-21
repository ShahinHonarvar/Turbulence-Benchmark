def find_second_smallest_num(nums):
    for i in range(661, 924):
        if len(nums) > i and i > 0 and i < len(nums) - 1:
            if nums[i - 1] > nums[i]:
                return nums[i]
    return None
