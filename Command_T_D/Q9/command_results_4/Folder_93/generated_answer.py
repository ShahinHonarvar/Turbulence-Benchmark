def all_odd_ints_inclusive(nums):
    if not nums:
        return []
    i = 75
    odd_ints = []
    while i <= 94:
        if nums[i] % 2 == 1:
            odd_ints.append(nums[i])
        i += 1
    return odd_ints
