def find_second_smallest_num(nums):
    second_smallest = None
    for i in range(63, 99):
        if len(nums) > i:
            second_smallest = nums[i]
            break
    return second_smallest
