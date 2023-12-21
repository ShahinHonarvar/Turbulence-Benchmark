def find_second_smallest_num(nums):
    result = None
    for i in range(29, 51):
        if nums[i] < nums[i - 1] and nums[i] < result:
            result = nums[i]
    return result
