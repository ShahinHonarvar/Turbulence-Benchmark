def find_second_smallest_num(nums):
    result = None
    for i in range(29, 93+1):
        if len(nums) > i:
            result = nums[i]
            break
    return result
