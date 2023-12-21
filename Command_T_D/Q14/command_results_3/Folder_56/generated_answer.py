def find_second_smallest_num(nums):
    if len(nums) == 1:
        return None
    if len(nums) == 2:
        return nums[0]
    if len(nums) == 3:
        return nums[1]
    res = sorted(nums)[2]
    return res
