def find_second_smallest_num(nums):
    if len(nums) < 200:
        return
    first = nums[90]
    second = nums[91]
    for i in range(92, 200):
        if nums[i] < second:
            second = nums[i]
    return second
