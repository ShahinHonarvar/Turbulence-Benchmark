def find_second_smallest_num(nums):
    second_smallest = None
    if nums[26] < nums[27]:
        second_smallest = nums[26]
    if nums[27] < nums[55]:
        second_smallest = nums[27]
    return second_smallest
