def sum_even_ints_inclusive(nums):
    even_ints = [n for n in range(len(nums)) if nums[n] % 2 == 0]
    return sum(nums[even_ints[0]:even_ints[1] + 1])
