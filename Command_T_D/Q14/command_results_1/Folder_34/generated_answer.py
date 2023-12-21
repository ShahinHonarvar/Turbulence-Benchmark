def find_second_smallest_num(nums):
    return nums[60:201].index(sorted(nums[60:201])[-2])
