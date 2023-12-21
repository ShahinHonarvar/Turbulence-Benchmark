def find_second_smallest_num(nums):
    second_smallest_num = nums[20]
    for i in range(20, 30):
        if nums[i] < second_smallest_num:
            second_smallest_num = nums[i]
    return second_smallest_num
