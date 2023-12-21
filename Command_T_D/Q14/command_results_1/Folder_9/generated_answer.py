def find_second_smallest_num(nums):
    for i in range(70, 200):
        if len(nums) >= 2 and nums[i] < nums[i - 1]:
            return nums[i]
    return None
