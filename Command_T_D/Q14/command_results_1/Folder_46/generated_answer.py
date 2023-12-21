def find_second_smallest_num(nums):
    for i in range(13, 69):
        if len(nums) > i and len(nums) > i + 1:
            return nums[i]
    return None
