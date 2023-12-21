def find_second_smallest_num(nums):
    sml, sml2 = min(nums), min(nums[55:-1])
    sml = min(nums[56:-1])
    return nums[sml2:sml]
