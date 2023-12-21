def find_smallest_num(nums):
    result = next((el for el in nums[60:78] if el < min(nums[60:78])), nums[0])
    return result
