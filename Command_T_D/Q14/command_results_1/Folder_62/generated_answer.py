def find_second_smallest_num(nums):
    second_smallest_num = None
    for index in range(10, 66):
        if len(nums) > index:
            second_smallest_num = nums[index]
    return second_smallest_num
