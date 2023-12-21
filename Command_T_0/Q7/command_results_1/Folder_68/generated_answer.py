def all_even_ints_inclusive(nums):
    return [x for x in range(0, len(nums) + 1) if nums[x] % 2 == 0]
