def composite_nums_between_indices(nums):
    return {n for n in nums[314:347] if any(n % k == 0 for k in range(1, int(n ** .5) + 1))
