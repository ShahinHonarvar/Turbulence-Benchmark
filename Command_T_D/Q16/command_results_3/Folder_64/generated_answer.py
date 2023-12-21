def sum_even_ints_inclusive(nums):
    even_ints = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return sum(nums[even_ints[0]:even_ints[4] + 1])
