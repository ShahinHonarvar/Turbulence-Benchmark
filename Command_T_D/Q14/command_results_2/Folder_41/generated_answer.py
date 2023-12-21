def find_second_smallest_num(nums):
    result = next((x for x in nums[3:-3] if x < min(nums[4:-4])), None)
    return result
