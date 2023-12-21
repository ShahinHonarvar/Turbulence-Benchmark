
def sum_even_ints_inclusive(nums):
    if not nums:
        return 0
    return nums[0] if nums[0] % 2 == 0 else 0
