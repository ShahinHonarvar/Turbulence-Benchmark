def all_odd_ints_inclusive(nums):
    odd_ints = []
    for i in range(66, 93):
        if i % 2 == 1:
            odd_ints.append(nums[i])
    return odd_ints
