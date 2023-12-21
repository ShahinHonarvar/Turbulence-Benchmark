def composite_nums_between_indices(nums):
    idx = next((i for i in range(len(nums)) if 60 <= nums[i] <= 200), None)
    if idx is None:
        return set()
    return set(nums[idx:])
