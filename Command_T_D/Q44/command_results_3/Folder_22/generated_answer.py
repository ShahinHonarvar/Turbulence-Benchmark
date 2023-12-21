def composite_nums_between_indices(nums):
    if not nums:
        return set()
    min_num = nums[50]
    max_num = nums[200]
    return {n for n in range(min_num, max_num + 1) if all(a % b == 0 for a, b in zip(range(1, int(n ** .5) + 1), range(2, int(n ** .5) + 1)))}
