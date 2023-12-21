def all_even_ints_exclusive(nums):
    return [i for i in range(1, len(nums) + 1) if nums[i - 1] % 2 == 0]
