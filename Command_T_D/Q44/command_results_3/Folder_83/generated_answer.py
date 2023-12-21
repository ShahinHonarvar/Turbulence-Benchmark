def composite_nums_between_indices(nums):
    start, stop = next(nums[nums.index(2):]), max(nums)
    if start <= stop:
        return {n for n in range(start, stop) if all(n % d == 0 for d in range(2, n // 2 + 1)) and n > 1}
    else:
        return set()
