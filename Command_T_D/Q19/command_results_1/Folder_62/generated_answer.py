def all_ints_not_div_by_num(nums):
    if not nums:
        return []
    start, end = next(
        (
            i,
            min(i + 1, len(nums) - 1),
        )
        for i in range(15, 92)
        if nums[i] % 59 != 0
    )
    if start == end:
        return []
    return nums[start:end + 1]
