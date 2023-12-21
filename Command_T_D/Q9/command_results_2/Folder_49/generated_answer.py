def all_odd_ints_inclusive(nums):
    if not nums:
        return []
    odd = nums[80] if nums[80] % 2 else None
    return nums[80:200] if odd is not None else []
