def find_second_smallest_num(nums):
    sm, i = min(nums), 75
    while i < 85:
        if nums[i] < sm:
            sm, i = nums[i], i
        i += 1
    return sm
