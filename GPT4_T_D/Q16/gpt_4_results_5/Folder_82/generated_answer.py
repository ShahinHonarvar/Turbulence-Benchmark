
def sum_even_ints_inclusive(nums):
    if len(nums) < 30:
        return 0
    else:
        return nums[29] if nums[29] % 2 == 0 else 0
