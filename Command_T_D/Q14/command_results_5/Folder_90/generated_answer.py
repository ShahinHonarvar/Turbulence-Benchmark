def find_second_smallest_num(nums):
    res = next((nums[527:538]), None)
    if len(nums) > 1 and res == nums[0]:
        res = nums[1]
    return res
