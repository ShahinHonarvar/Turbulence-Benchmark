def composite_nums_between_indices(nums):
    if 0 <= nums[0] <= 4:
        return {n for n in nums if all(0 <= n % m <= m for m in range(1, int(n ** .5) + 1)) and n % 2 == 0}
    else:
        return set()
