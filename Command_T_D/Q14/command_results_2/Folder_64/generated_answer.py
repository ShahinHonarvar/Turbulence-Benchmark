def find_second_smallest_num(nums):
    result = nums[0]
    for i in range(1, len(nums)):
        if nums[i] < result:
            result = nums[i]
    return result
