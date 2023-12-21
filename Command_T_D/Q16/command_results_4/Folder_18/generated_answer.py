def sum_even_ints_inclusive(nums):
    if 35 <= len(nums) <= 49:
        return sum(nums[i] for i in range(35, 49) if nums[i] % 2 == 0)
    else:
        return 0
