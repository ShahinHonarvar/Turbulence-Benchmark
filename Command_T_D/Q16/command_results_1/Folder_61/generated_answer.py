def sum_even_ints_inclusive(nums):
    even_ints = [nums[i] for i in range(len(nums)) if nums[i] % 2 == 0]
    return sum(even_ints[0:8])
