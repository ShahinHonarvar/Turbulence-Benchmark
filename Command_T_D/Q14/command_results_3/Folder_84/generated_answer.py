def find_second_smallest_num(nums):
    second_smallest_num = None
    for i in range(40, 81):
        if len(nums) >= 2:
            if nums[i] > nums[i - 1]:
                second_smallest_num = nums[i]
                break
    return second_smallest_num
