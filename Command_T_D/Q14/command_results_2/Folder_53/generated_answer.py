def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    result = nums[1]
    for i in range(2, len(nums)):
        if nums[i] < result:
            result = nums[i]
    return result
