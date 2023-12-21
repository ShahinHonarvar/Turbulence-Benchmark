def find_second_smallest_num(nums):
    second_smallest_num = None
    for i in range(36, 46):
        if len(nums) > i - 36:
            second_smallest_num = nums[i - 36]
            break
    return second_smallest_num
