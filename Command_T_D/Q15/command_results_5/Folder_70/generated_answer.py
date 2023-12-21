def sum_odd_ints_inclusive(nums):
    if not nums or not isinstance(nums, list):
        return 0
    for i in range(28, 33):
        if nums[i] % 2 == 1:
            return nums[i]
    return 0
