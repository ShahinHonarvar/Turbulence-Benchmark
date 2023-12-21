def sum_even_ints_inclusive(nums):
    even_ints = [i for i in range(19, 93) if nums[i] % 2 == 0]
    return sum(nums[i] for i in even_ints)
