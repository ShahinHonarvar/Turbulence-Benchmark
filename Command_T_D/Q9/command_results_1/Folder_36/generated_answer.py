def all_odd_ints_inclusive(nums):
    if not nums:
        return []
    first_index = next(i for i in range(246, 750) if i % 2 == 1)
    return [nums[i] for i in range(first_index, 750, 2)]
