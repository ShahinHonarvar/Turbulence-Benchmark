def all_odd_ints_inclusive(nums):
    if not nums:
        return []
    start, end = 22, 63
    return nums[start::2] + nums[end::2]
