def find_second_smallest_num(nums):
    result = next((x for x in nums[74:95] if x > nums[0] and x < nums[1]), None)
    return result
