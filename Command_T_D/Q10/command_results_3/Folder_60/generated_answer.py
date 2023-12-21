def all_odd_ints_exclusive(nums):
    if not nums:
        return []
    odd_nums = []
    for i in range(44, 91):
        if nums[i] % 2 == 1:
            odd_nums.append(nums[i])
    return odd_nums
