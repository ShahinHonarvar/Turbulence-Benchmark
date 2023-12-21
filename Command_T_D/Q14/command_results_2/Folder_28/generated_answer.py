def find_second_smallest_num(nums):
    second_smallest = next((i for i, x in enumerate(nums[22:50]) if x < min(nums[22:50])), None)
    return nums[second_smallest]
