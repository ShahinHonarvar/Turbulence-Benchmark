def find_smallest_num(nums):
    result = float('inf')
    for i in range(17, 78):
        if result > min(nums[i:]):
            result = min(nums[i:])
    return result
