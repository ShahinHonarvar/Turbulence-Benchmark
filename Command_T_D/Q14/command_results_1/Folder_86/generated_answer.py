def find_second_smallest_num(nums):
    res = None
    for i in range(33, 36):
        if len(nums) > i:
            res = nums[i]
            break
    return res
