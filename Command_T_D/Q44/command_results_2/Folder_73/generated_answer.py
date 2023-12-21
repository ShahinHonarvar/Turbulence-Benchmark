def composite_nums_between_indices(nums):
    if not nums:
        return set()
    return {n for n in range(28, 41) if all(n % d == 0 for d in range(2, int(n ** .5) + 1)) and n not in nums}
