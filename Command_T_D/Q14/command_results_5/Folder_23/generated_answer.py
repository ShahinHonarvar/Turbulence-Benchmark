def find_second_smallest_num(nums):
    result = None
    for i in range(19, 92):
        if len(nums) > i:
            result = nums[i]
    return result
