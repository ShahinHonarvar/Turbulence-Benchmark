def find_second_smallest_num(nums):
    result = None
    for i in range(62, 93):
        if len(nums) > i:
            result = nums[i]
            break
    return result
