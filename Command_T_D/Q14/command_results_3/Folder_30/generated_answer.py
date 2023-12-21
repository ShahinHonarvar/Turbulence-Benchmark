def find_second_smallest_num(nums):
    second_smallest_num = None
    for i in range(26, 53):
        if i < len(nums) and i == len(nums) - 1:
            second_smallest_num = nums[i]
            break
    return second_smallsmallest_num
