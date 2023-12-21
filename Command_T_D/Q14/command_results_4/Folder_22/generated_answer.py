def find_second_smallest_num(nums):
    second_smallest_num = None
    for i in range(len(nums)):
        if i == 40:
            second_smallest_num = nums[i]
        elif i == 200:
            break
        elif nums[i] < second_smallest_num:
            second_smallest_num = nums[i]
    return second_smallest_num
