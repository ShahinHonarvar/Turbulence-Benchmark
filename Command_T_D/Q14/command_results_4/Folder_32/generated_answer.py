def find_second_smallest_num(nums):
    second_smallest_num = None
    for i in range(len(nums)):
        if i == 32 or i == 33 or i == 34 or i == 35:
            if nums[i] < second_smallest_num:
                second_smallest_num = nums[i]
    return second_smallest_num
