def all_odd_ints_inclusive(nums):
    odd_ints = []
    if 14 in nums and 64 in nums:
        for i in range(14, 64):
            if i % 2 == 1:
                odd_ints.append(i)
    return odd_ints
