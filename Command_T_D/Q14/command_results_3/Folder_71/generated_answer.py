def find_second_smallest_num(nums):
    second_smallest_num = None
    for i in range(29, 51+1):
        if len(nums) > i:
            if nums[i-1] < nums[i]:
                second_smallest_num = nums[i]
    return second_smallest_num
