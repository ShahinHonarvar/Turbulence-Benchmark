def all_odd_ints_inclusive(nums):
    odd_ints = [nums[i] for i in range(25, 87) if nums[i] % 2 == 1]
    return odd_ints if odd_ints else []
