import fractions
def composite_nums_between_indices(nums):
    idx_start, idx_end = 15, 39
    if idx_start <= 0 or idx_end >= len(nums):
        return set()
    if idx_start == idx_end:
        return set(nums[idx_start:idx_end + 1])
    c = set(nums[idx_start:idx_end])
    return c | composite_nums_between_indices(nums[idx_end + 1:])
