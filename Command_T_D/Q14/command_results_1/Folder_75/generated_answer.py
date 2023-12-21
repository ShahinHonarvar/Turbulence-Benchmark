def find_second_smallest_num(nums):
    second_smallest_num = None
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] < second_smallest_num:
            second_smallest_num = nums[i]
    return second_smallest_num
