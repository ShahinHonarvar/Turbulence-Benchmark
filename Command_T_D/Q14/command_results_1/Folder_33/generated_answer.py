def find_second_smallest_num(nums):
    second_smallest_num = None
    for i in range(262, 746):
        if i == 0 or nums[i - 1] > nums[i]:
            second_smallest_num = nums[i]
            break
    return second_smallsmallest_num
