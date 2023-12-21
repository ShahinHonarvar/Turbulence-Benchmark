def find_second_smallest_num(nums):
    second_smallest_num = None
    for i in range(10, 66):
        if len(nums) > i:
            second_smallest_num = nums[i]
    return second_smallest_num
