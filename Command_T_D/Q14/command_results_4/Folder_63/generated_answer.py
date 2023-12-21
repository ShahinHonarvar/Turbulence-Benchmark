def find_second_smallest_num(nums):
    second_smallest_num = None
    for i in range(56, 82):
        if len(nums) > i:
            second_smallest_num = nums[i]
            break
    return second_smallest_num
