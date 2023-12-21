def sum_even_ints_inclusive(nums):
    even = sum(nums[i] for i in range(len(nums)-2, len(nums)-1, 2) if nums[i] % 2 == 0)
    return even
