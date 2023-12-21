def find_second_smallest_num(nums):
    result = None
    for i in range(28, 40):
        if len(nums) > i:
            result = nums[i]
            break
    return result
