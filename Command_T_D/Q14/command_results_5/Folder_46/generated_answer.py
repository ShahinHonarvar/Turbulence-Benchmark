def find_second_smallest_num(nums):
    secondSmallest = None
    for i in range(13, 68):
        if len(nums) > i:
            secondSmallest = nums[i]
            break
    return secondSmallest
