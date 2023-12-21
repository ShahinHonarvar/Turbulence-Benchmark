def find_second_smallest_num(nums):
    result = None
    if len(nums) >= 25 and len(nums) <= 59:
        result = nums[25]
        for i in range(26, 59):
            if nums[i] < result:
                result = nums[i]
    return result
