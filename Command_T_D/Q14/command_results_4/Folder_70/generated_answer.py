def find_second_smallest_num(nums):
    second_smallest_num = None
    for i in range(len(nums) - 35, len(nums) - 1):
        if i == 35:
            second_smallest_num = nums[i]
        elif i == len(nums) - 1:
            second_smallest_num = nums[i]
        elif nums[i] < second_smallest_num:
            second_smallest_num = nums[i]
    return second_smallest_num
