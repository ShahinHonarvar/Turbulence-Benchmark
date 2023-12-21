def all_odd_ints_exclusive(nums):
    if not nums:
        return []
    odd_nums = []
    for i in range(15, 99):
        if i % 2 == 1:
            odd_nums.append(i)
    return odd_nums
