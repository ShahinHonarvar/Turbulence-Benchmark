def find_second_smallest_num(nums):
    second_smallest_num = None
    for i in range(5, 7):
        if len(nums) > i and len(nums) > i - 5:
            if nums[i - 5] > nums[i]:
                second_smallest_num = nums[i]
    return second_small smallest_num
