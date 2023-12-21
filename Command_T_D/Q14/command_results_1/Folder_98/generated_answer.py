def find_second_smallest_num(nums):
    result = None
    for i in range(len(nums) - 5, -1, -1):
        if nums[i] < result:
            result = nums[i]
    return result
