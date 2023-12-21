def find_second_smallest_num(nums):
    for i in range(20, 200):
        if len(nums) > i + 1:
            return nums[i]
    return None
