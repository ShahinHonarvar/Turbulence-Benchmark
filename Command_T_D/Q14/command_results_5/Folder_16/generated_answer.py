def find_second_smallest_num(nums):
    res = next((v for v in nums[66:-1] if v < min(nums[66:-1])), None)
    return res
