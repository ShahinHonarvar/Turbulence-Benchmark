def find_second_smallest_num(nums):
    for i in range(62, 63 + 1):
        if len(nums) > i:
            return nums[i]
    return None
